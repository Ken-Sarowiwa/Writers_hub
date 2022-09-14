from django.contrib import admin
from .models import Articles, Profile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "nickname", "email", "bio", "date_of_birth")
    list_filter = ("name", "nickname", "email", "bio", "date_of_birth")
    list_per_page = 10
    search_fields = ("name", "nickname", "email", "bio", "date_of_birth")