from django.shortcuts import render
from rest_framework import permissions, status, generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMultiAlternatives
from .serializers import UserRegisterSerializer, UserResetPasswordSerializer, UserPasswordSerializer, GameListSerializer, TeamSerializer, CurrentCheckPointSerializer, CheckPointCoordinatesSerializer, ProfileInfoSerializer
from django.utils.html import strip_tags
from django.contrib.auth.password_validation import validate_password
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from .models import Game, Team, Gamer, Profile, InvitationToken, CurrentCheckPoint, CheckPoint
from django.conf import settings
from django.utils import timezone
from hashlib import sha1
import six
import threading
import math

class EmailTokenGenerator(PasswordResetTokenGenerator):
	def _make_hash_value(self, user, timestamp):
		return(six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active))

email_token_gen = EmailTokenGenerator()
password_token_gen = PasswordResetTokenGenerator()

def list_to_queryset(model_list):
    if len(model_list) > 0:
        return model_list[0].__class__.objects.filter(
                    pk__in=[obj.pk for obj in model_list])
    else:
        return []

class ListGamesAPIView(generics.ListAPIView):
	serializer_class = GameListSerializer
	permission_classes = [permissions.IsAuthenticated]
	filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
	filterset_fields = ['co_op','max_gamers','active','average_time']
	ordering_fields = ['max_gamers','active','average_time','name']
	search_fields = ['name', 'description']

	def get_queryset(self):
		profile = Profile.objects.get(user = self.request.user)
		data = []
		for game_i in Game.objects.filter(active = True):
			teams = game_i.teams.all()
			if(self.kwargs['visited'] == '0'):
				test = True
				for team_i in teams:
					gamer_i = Gamer.objects.filter(team = team_i, profile = profile)
					if(gamer_i.exists()):
						test = False
						break
				if(test):
					data.append(game_i)
			else:
				test = False
				for team_i in teams:
					gamer_i = Gamer.objects.filter(team = team_i, profile = profile)
					if(gamer_i.exists()):
						test = True
						break
				if(test):
					data.append(game_i)
		if(len(data)!=0):
			return list_to_queryset(data)
		else:
			return Game.objects.none()

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def SingleGameAPIView(request, slug):
	game = Game.objects.filter(slug = slug)
	if(game.exists()):
		profile = Profile.objects.get(user = request.user)
		game = game.first()
		teams = Team.objects.filter(game = game)
		team = []
		for team_i in teams:
			if(Gamer.objects.filter(profile = profile, team = team_i).exists()):
				team = team_i
				break
		if(team):
			serializer = TeamSerializer(team)
			data = serializer.data
			gamers = data['gamers']
			can_start = False
			invite_token = ''
			if(not team.active):
				if(team.captain == profile and (not game.co_op or len(gamers) == game.max_gamers) and not team.finished):
					can_start = True
				if(team.captain == profile and len(gamers) != game.max_gamers and not team.finished):
					invite = InvitationToken.objects.filter(team = team)
					if(invite.exists()):
						invite = invite.first()
						invite_token = invite.token
				if(team.finished):
					done_chepoints = []
					cur_checkpoint = CurrentCheckPoint.objects.get(team = team).check_point
					temp_check_point = CheckPoint.objects.get(game = team.game, start = True)
					done_chepoints.append(CheckPointCoordinatesSerializer(temp_check_point).data)
					while temp_check_point.id!=cur_checkpoint.id:
						temp_check_point = temp_check_point.next_checkpoint
						done_chepoints.append(CheckPointCoordinatesSerializer(temp_check_point).data)
					return Response({'ok':True, 'can_take_part':False, 'can_start':can_start, 'invite_token':invite_token, **data, 'done_chepoints':done_chepoints}, status = status.HTTP_200_OK)
				return Response({'ok':True, 'can_take_part':False, 'can_start':can_start, 'invite_token':invite_token, **data}, status = status.HTTP_200_OK)
			else:
				done_chepoints = []
				cur_checkpoint = CurrentCheckPoint.objects.get(team = team).check_point
				cur_checkpoint_serializer = CurrentCheckPointSerializer(cur_checkpoint)
				temp_check_point = CheckPoint.objects.get(game = team.game, start = True)
				done_chepoints.append(CheckPointCoordinatesSerializer(temp_check_point).data)
				while temp_check_point.id!=cur_checkpoint.id:
					temp_check_point = temp_check_point.next_checkpoint
					done_chepoints.append(CheckPointCoordinatesSerializer(temp_check_point).data)
				return Response({'ok':True, 'can_take_part':False, 'can_start':can_start, 'invite_token':invite_token, **data, 'current_checkpoint':cur_checkpoint_serializer.data, 'done_chepoints':done_chepoints}, status = status.HTTP_200_OK)
		else:
			serializer = GameListSerializer(game)
			data = serializer.data
			return Response({'ok':True, 'can_take_part':True, **serializer.data}, status = status.HTTP_200_OK)
	return Response({'ok':False, 'error':'Game does not exist'}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def CloseCheckPointAPIView(request, slug):
	game = Game.objects.filter(slug = slug)
	if(game.exists()):
		profile = Profile.objects.get(user = request.user)
		game = game.first()
		teams = Team.objects.filter(game = game)
		team = []
		for team_i in teams:
			if(Gamer.objects.filter(profile = profile, team = team_i).exists()):
				team = team_i
				break
		if(team):
			temp_check_point = CheckPointCoordinatesSerializer(data = request.data)
			if(temp_check_point.is_valid() and team.active and not team.finished):
				temp_check_point = temp_check_point.validated_data
				cur_checkpoint = CurrentCheckPoint.objects.get(team = team)
				dest = math.sqrt((temp_check_point['coordinates_lat']-cur_checkpoint.check_point.next_checkpoint.coordinates_lat)**2 + (temp_check_point['coordinates_lon']-cur_checkpoint.check_point.next_checkpoint.coordinates_lon)**2)
				if(dest<settings.MAX_CHECK_RADIUS):
					cur_checkpoint.check_point = cur_checkpoint.check_point.next_checkpoint
					cur_checkpoint.save()
					if(cur_checkpoint.check_point.last):
						team.active = False
						team.finished = True
						team.end = timezone.now()
						team.save()
						for gamer in team.gamers.all():
							temp_prof = gamer.profile
							temp_prof.points += game.points
							temp_prof.save()
					return Response({'ok':True}, status = status.HTTP_200_OK)
				return Response({'ok':False, 'error':'You are too far from the place'}, status = status.HTTP_400_BAD_REQUEST)
			return Response({'ok':False, 'error':temp_check_point.errors if temp_check_point.errors else 'Game finished' }, status = status.HTTP_400_BAD_REQUEST)
		return Response({'ok':False, 'error':'You do not take part in game'}, status = status.HTTP_400_BAD_REQUEST)
	return Response({'ok':False, 'error':'Game does not exist'}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def GameTakePartAPIView(request, slug):
	game = Game.objects.filter(slug = slug)
	if(game.exists()):
		game = game.first()
		profile = Profile.objects.get(user = request.user)
		teams = Team.objects.filter(game = game)
		team = []
		for team_i in teams:
			if(Gamer.objects.filter(profile = profile, team = team_i).exists()):
				team = team_i
				break
		if(not team):
			team = Team.objects.create(game = game, captain = profile)
			if(game.co_op):
				invite_token = sha1(bytes(f'{team.id}{game.id}{profile.id}{profile.user.username}','utf-8')).hexdigest()[:200]
				InvitationToken.objects.create(team = team, token = invite_token)
			gamer = Gamer.objects.create(team = team, profile = profile)
			return Response({'ok':True}, status = status.HTTP_200_OK)
		return Response({'ok':False, 'error':'You alredy take part in this game'}, status = status.HTTP_400_BAD_REQUEST)
	return Response({'ok':False, 'error':'Game does not exist'}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def JoinTeamAPIView(request, slug, token):
	game = Game.objects.filter(slug = slug)
	if(game.exists()):
		invite = InvitationToken.objects.filter(token = token)
		if(invite.exists()):
			profile = Profile.objects.get(user = request.user)
			invite = invite.first()
			team = invite.team
			serializer = TeamSerializer(team)
			gamers = serializer.data['gamers']
			if(len(gamers) < team.game.max_gamers):
				Gamer.objects.create(team = team, profile = profile)
				return Response({'ok':True},status = status.HTTP_200_OK)
			return Response({'ok':False, 'error':'Game finished or team is full'}, status = status.HTTP_400_BAD_REQUEST)
		return Response({'ok':False, 'error':'Invalid invite link'}, status = status.HTTP_400_BAD_REQUEST)
	return Response({'ok':False, 'error':'Game does not exist'}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def StartGameAPIView(request,slug):
	game = Game.objects.filter(slug = slug)
	if(game.exists()):
		game = game.first()
		profile = Profile.objects.get(user = request.user)
		teams = Team.objects.filter(game = game, captain = profile)
		team = []
		for team_i in teams:
			if(Gamer.objects.filter(profile = profile, team = team_i).exists()):
				team = team_i
				break
		if(team):
			if(team.captain == profile and not team.finished and not team.active):
				team.active = True
				team.start = timezone.now()
				team.save()
				first_check_point = CheckPoint.objects.get(game = team.game, start = True)
				cur_checkpoint = CurrentCheckPoint.objects.create(team = team, check_point = first_check_point)
				return Response({'ok':True}, status = status.HTTP_200_OK)
			return Response({'ok':False, 'error':'You are not a captain or game finished or game in progress'}, status = status.HTTP_400_BAD_REQUEST)
		return Response({'ok':False, 'error':'You do not take part in game'}, status = status.HTTP_400_BAD_REQUEST)
	return Response({'ok':False, 'error':'Game does not exist'}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([~permissions.IsAuthenticated])
def UserRegisterAPIView(request):
	serializer = UserRegisterSerializer(data = request.data)
	if(serializer.is_valid()):
		data = serializer.validated_data
		if(User.objects.filter(username = data['username']).exists() or User.objects.filter(email = data['email']).exists()):
			return Response({'ok':False, 'error':'User already exists'}, status = status.HTTP_400_BAD_REQUEST)
		try:
			validate_password(data['password'])
		except Exception as errors:
			return Response({'ok':False, 'error':errors}, status = status.HTTP_400_BAD_REQUEST)
		user = User.objects.create(username = data['username'], email = data['email'], is_active = False)
		user.set_password(data['password'])
		user.save()
		domain = get_current_site(request).domain
		mail_subject = 'Account activation'
		message = render_to_string('email_activtion.html',{
			'user':user,
			'domain': domain,
            'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': email_token_gen.make_token(user),
		})
		message_task = threading.Thread(target = async_email_send, args=( mail_subject, message, [data['email']] ))
		message_task.start()
		return Response({'ok':True}, status = status.HTTP_200_OK)
	return Response({'ok':False, 'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def UserActivationAPIView(request, uidb64, token):
	uid = force_text(urlsafe_base64_decode(uidb64))
	user = User.objects.filter(id = uid)
	if(user.exists()):
		user = user.first()
		if(email_token_gen.check_token(user, token)):
			user.is_active = True
			user.save()
			return Response({'ok':True}, status = status.HTTP_200_OK)
	return Response({'ok':False, 'error':'Invalid activation link'}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([~permissions.IsAuthenticated])
def UserResetPasswordRequestAPIView(request):
	serializer = UserResetPasswordSerializer(data = request.data)
	if(serializer.is_valid()):
		data = serializer.validated_data
		user = User.objects.filter(email = data['email'])
		if(user.exists()):
			user = user.first()
			domain = get_current_site(request).domain
			mail_subject = 'Password reset'
			message = render_to_string('password_reset.html',{
				'user':user,
				'domain': domain,
	            'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
	            'token': password_token_gen.make_token(user),
			})
			message_task = threading.Thread(target = async_email_send, args=( mail_subject, message, [data['email']] ))
			message_task.start()
			return Response({'ok':True}, status = status.HTTP_200_OK)
		return Response({'ok':False, 'error':'User does not exist'}, status = status.HTTP_400_BAD_REQUEST)
	return Response({'ok':False, 'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([~permissions.IsAuthenticated])
def UserResetPasswordAPIView(request, uidb64, token):
	serializer = UserPasswordSerializer(data = request.data)
	if(serializer.is_valid()):
		data = serializer.validated_data
		try:
			validate_password(data['password'])
		except Exception as errors:
			return Response({'ok':False, 'error':errors}, status = status.HTTP_400_BAD_REQUEST)
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.filter(id = uid)
		if(user.exists()):
			user = user.first()
			if(password_token_gen.check_token(user, token)):
				user.set_password(data['password'])
				user.save()
				return Response({'ok':True}, status = status.HTTP_200_OK)
			return Response({'ok':False, 'error':'Invalid password reset link'}, status = status.HTTP_400_BAD_REQUEST)
		return Response({'ok':False, 'error':'User does not exist'}, status = status.HTTP_400_BAD_REQUEST)
	return Response({'ok':False, 'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def ProfileInfoAPIView(request):
	profile = Profile.objects.get(user = request.user)
	serializer = ProfileInfoSerializer(profile)
	return Response({'ok':True, **serializer.data}, status = status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def UserLogoutAPIView(request):
	Token.objects.get(user = request).delete()
	return Response(status = status.HTTP_200_OK)

def async_email_send(mail_subject, message, to_email):
	mail_to_send = EmailMultiAlternatives(mail_subject, strip_tags(message), to=to_email)
	mail_to_send.attach_alternative(message, 'text/html')
	mail_to_send.send()