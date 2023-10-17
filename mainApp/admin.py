from . import models
from django.contrib import admin

admin.site.register(models.Positions)


class MemberGamesAdminInline(admin.StackedInline):
    model = models.MemberGames


class MemberTrainsAdminInline(admin.StackedInline):
    model = models.MemberTrains


class GamesAdmin(admin.ModelAdmin):
    list_display = ["owners", "guests", "datetime"]
    list_filter = ["datetime"]
    search_fields = ["owner", "guest"]


admin.site.register(models.Game, GamesAdmin)


class TrainsAdmin(admin.ModelAdmin):
    list_display = ["team", "date"]
    list_filter = ["date"]
    search_fields = ["team"]


admin.site.register(models.Train, TrainsAdmin)


class TeamsAdmin(admin.ModelAdmin):
    list_display = ["name", "owner", "coach"]
    search_fields = ["name", "owner", "coach"]


admin.site.register(models.Team, TeamsAdmin)


class MembersAdmin(admin.ModelAdmin):
    list_display = ["name", "team", "position"]
    list_filter = ["team", "position"]
    search_fields = ["name"]
    inlines = [MemberTrainsAdminInline, MemberGamesAdminInline]


admin.site.register(models.Member, MembersAdmin)
