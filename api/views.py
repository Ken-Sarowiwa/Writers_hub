from django.shortcuts import render
from .models import Profile, Articles
from rest_framework import viewsets, permissions
from .serializers import ProfileSerializer, ArticleSerializer
# Create your views here.

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

