from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Game, Team, Gamer

class GameListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Game
		fields = '__all__'

class UserRegisterSerializer(serializers.ModelSerializer):
	email = serializers.EmailField(required=True)
	class Meta:
		model = User
		fields = [
			'username',
			'password',
			'email'
		]

class TeamSerializer(serializers.ModelSerializer):
	game = serializers.SerializerMethodField()
	gamers = serializers.SerializerMethodField()
	captain = serializers.SerializerMethodField()
	class Meta:
		model = Team
		fields = [
			'active',
			'finished',
			'start',
			'end',
			'captain',
			'game',
			'gamers',
		]
	def get_game(self, obj):
		return(GameListSerializer(obj.game).data)
	def get_gamers(self, obj):
		return(list(map(lambda ob:ob.profile.user.username,Gamer.objects.filter(team = obj))))
	def get_captain(self, obj):
		return(obj.captain.user.username)

class UserResetPasswordSerializer(serializers.ModelSerializer):
	email = serializers.EmailField(required=True)
	class Meta:
		model = User
		fields = [
			'email'
		]

class UserPasswordSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = [
			'password'
		]