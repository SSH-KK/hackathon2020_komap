from django.contrib import admin
from . import models

admin.site.register(models.Profile)
admin.site.register(models.CheckPoint)
admin.site.register(models.Game)
admin.site.register(models.InvitationToken)
admin.site.register(models.Gamer)
admin.site.register(models.Team)
# Register your models here.
