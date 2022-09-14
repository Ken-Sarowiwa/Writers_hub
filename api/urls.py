from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from api import views
from .views import UserViewSet, GroupViewSet, ArticlesViewSet, ProfileViewSet

router = routers.DefaultRouter()

router.register(r"users", views.UserViewSet)
router.register(r"articles", views.ArticlesViewSet)
router.register(r"profiles", views.ProfileViewSet)

urlpatterns = [
    path("" , include(router.urls)),
    path("api/articles", ArticlesViewSet.as_view({"get": "list"})),
    path("api/profiles", ProfileViewSet.as_view({"get": "list"})),
    path("api/users", UserViewSet.as_view({"get":"list"})),

]