from django.contrib import admin
from .models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('get_username','get_full_name')

admin.site.register(Profile, ProfileAdmin)