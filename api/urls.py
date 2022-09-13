from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from api import views
from .views import UserViewSet, GroupViewSet, ArticlesViewSet

router = routers.DefaultRouter()

router.register(r"users", views.UserViewSet)
router.register(r"articles", views.ArticlesViewSet)
router.register(r"profiles", views.ProfileViewSet)

url patterns = [
    path("" , include(router.urls)),
    path("api/articles", ArticlesViewSet.as_view({"get": "list"}))

]