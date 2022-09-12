from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Articles, Profile
from django.contrib.auth.models import User
from django.core.validators import validate_email


# class for the profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id", "name", "nickname", "avatar", "email", "bio", "date_of_birth")


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ("id", "username", "email", "profile")

        def create(self, validated_data):
            profile_data = validated_data.get("profile")
            user = User.objects.create_user(**validated_data)
            Profile.objects.create(user=user, **profile_data)
            user.set_password(validated_data["password"])
            user.set_password(validated_data["confirm_password"])
            user.save()
            return user

        def validate(self, validated_data):
            if validated_data["password"] != validated_data["confirm_password"]:
                raise serializers.ValidationError("passwords should match")
            if validated_data["email"] == "":
                raise serializers.ValidationError("please fill in your email")
            if User.objects.filter(email=validated_data["email"]).exists():
                raise serializers.ValidationError("email already exists")
            try :
                validate_email(validated_data["email"])
            except ValidationError:
                raise serializers.ValidationError("email is invalid")
            else:
                return validated_data

        def update(self, instance, validated_data):
            instance.username = validated_data.get("username", instance.username)
            instance.email = validated_data.get("email", instance.email)
            instance.password = validated_data.get("password", instance.password)
            instance.nickname = validated_data.get("nickname", instance.nickname)
            instance.avatar = validated_data.get("avatar", instance.avatar)
            instance.bio = validated_data.get("bio", instance.bio)
            instance.date_of_birth = validated_data.get("date_of_birth", instance.date_of_birth)
            instance.save()
            return instance

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ("id","title","content","author","date","image","likes","comment","share")

        def create(self, validated_data):
            article = Articles.Objects.create(**validated_data)
            article.save()
            return article

        def update(self, instance, validated_data):
            instance.title = validated_data.get("title", instance.title)
            instance.content = validated_data.get("content", instance.content)
            instance.photo = validated_data.get("photo", instance.photo)
            instance.comment = validated_data.get("comment", instance.comment)
            instance.save()
            return instance

