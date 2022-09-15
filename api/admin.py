from django.contrib import admin
from .models import Articles, Profile
# Register your models here.




class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "nickname", "email", "bio", "date_of_birth")
    list_filter = ("name", "nickname", "email", "bio", "date_of_birth")
    list_per_page = 10
    search_fields = ("name", "nickname", "email", "bio", "date_of_birth")
    ordering = ("name", "nickname", "email", "bio", "date_of_birth")


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "author", "date", "image", "comment", "share")
    list_filter = ("title", "content", "author", "date", "image", "likes", "comment", "share")
    list_per_page = 10
    search_fields = ("title", "content", "author", "date", "image", "likes", "comment", "share")
    ordering = ("title", "content", "author", "date", "image", "likes", "comment", "share")

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Articles, ArticleAdmin)