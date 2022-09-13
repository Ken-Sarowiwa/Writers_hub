from django.shortcuts import render
from rest_framework.response import Response

from .models import Profile, Articles
from rest_framework import viewsets, permissions, status
from .serializers import ProfileSerializer, ArticleSerializer, UserSerializer
# Create your views here.

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        profile = Profile.objects.filter(user=self.request.user)
        return profile

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return super(ProfileViewSet, self).retrieve(request)


class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        articles = Articles.objects.filter(author=self.request.user)
    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get-queryset()
        return super(ArticlesViewSet, self).retrieve(request)


class GroupViewSet:
    pass

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = User.objects.filter(user=self.request.user)
        return user

    def create(self, request, *args, **kwargs):
        user = User.objects.create_user(**validated_data)
        if