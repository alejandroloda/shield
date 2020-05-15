from django.contrib import admin
from . import models


# Register your models here.

class PowerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'level')


admin.site.register(models.Power, PowerAdmin)


class MetaHumanAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'active', 'level', 'ally')
    list_filter = ('active', 'level', 'ally')


admin.site.register(models.MetaHuman, MetaHumanAdmin)


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'headquarter')
    list_filter = (['headquarter'])


admin.site.register(models.Team, TeamAdmin)
