from django.contrib import admin

from common.models import HomeVideo


@admin.register(HomeVideo)
class HomeVideoAdmin(admin.ModelAdmin):
    list_display = ("name", )

