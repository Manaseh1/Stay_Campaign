from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_username','about_me',)
    def user_username(self, obj):
        return obj.user.username


@admin.register(Mangender)
class MangenderAdmin(admin.ModelAdmin):
    list_display = ('title',)