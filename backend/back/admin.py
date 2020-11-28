from django.contrib import admin
from . import models

admin.site.register(models.Profile)
admin.site.register(models.CheckPoint)
admin.site.register(models.Game)
# Register your models here.
