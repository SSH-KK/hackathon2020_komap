from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

CheckPointTypes = [
	('QR','QR Code'),
	('GPS','GPS Coordinates')
]

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	points = models.DecimalField(max_digits=7, decimal_places=0, default = 0)

	def __str__(self):
		return(f'{self.user.username} - {self.user.email}')

class Game(models.Model):
	title = models.CharField(max_length = 100, blank = False, null = False, unique = True)
	description = models.TextField(blank = False, null = False)
	average_time = models.DecimalField(max_digits = 4, decimal_places=0, blank = False, null = False)
	lenght = models.DecimalField(max_digits = 6, decimal_places= 0, blank = False, null = False)
	co_op = models.BooleanField(blank = False, null = False)
	max_gamers = models.DecimalField(max_digits = 3, decimal_places = 0, blank = False, null = False)
	active = models.BooleanField(default = True)
	points = models.DecimalField(max_digits = 3, decimal_places = 0, blank = False, null = False)
	slug = models.SlugField(unique = True, blank = True, null = False)

class CheckPoint(models.Model):
	check_type = models.CharField(choices = CheckPointTypes, max_length = 20, blank = False, null = False)
	name = models.CharField(max_length = 150, blank = False, null = False)
	coordinates_lat = models.DecimalField(max_digits = 8, decimal_places = 6, blank = True, null = True)
	coordinates_lon = models.DecimalField(max_digits = 8, decimal_places = 6, blank = True, null = True)
	description = models.TextField(blank = False, null = False)
	next_checkpoint = models.ForeignKey('self', on_delete = models.CASCADE, blank = True, null = True)
	qr_data = models.TextField(blank = True, null = True)
	last = models.BooleanField(default = False)
	start = models.BooleanField(default = False)
	address = models.CharField(max_length = 200, blank = True, null = True)
	game = models.ForeignKey(Game, on_delete = models.CASCADE, blank = False, null = False)

class Team(models.Model):
	game = models.ForeignKey(Game, on_delete= models.CASCADE,related_name = 'teams', blank = False, null = False)
	active = models.BooleanField(default = False)
	finished = models.BooleanField(default = False)
	start = models.DateTimeField(blank = True, null = True)
	end = models.DateTimeField(blank = True, null = True)
	captain = models.ForeignKey(Profile, on_delete = models.CASCADE, blank = True, null = True)

class InvitationToken(models.Model):
	token = models.CharField(max_length = 200, blank = False, null = False)
	team = models.ForeignKey(Team, on_delete = models.CASCADE, blank = False, null = False)

class Gamer(models.Model):
	profile = models.ForeignKey(Profile, on_delete = models.CASCADE, blank = False, null = False)
	team = models.ForeignKey(Team, on_delete = models.CASCADE, related_name = 'gamers', blank = False, null = False)

class CurrentCheckPoint(models.Model):
	team = models.ForeignKey(Team, on_delete = models.CASCADE, blank = False, null = False)
	check_point = models.ForeignKey(CheckPoint, on_delete = models.CASCADE, blank = False, null = False)

@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
	if(created):
		Profile.objects.create(user = instance)

@receiver(pre_save, sender = Game)
def add_game_slug(sender, instance, **kwargs):
	if(instance.slug == ''):
		instance.slug = f"{instance.title.replace(' ','_')}"