from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Cinema)
admin.site.register(models.City)
admin.site.register(models.Payment)
admin.site.register(models.User)
admin.site.register(models.CinemaHall)
admin.site.register(models.Movie)
