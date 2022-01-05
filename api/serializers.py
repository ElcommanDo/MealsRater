from rest_framework import serializers
from .models import Meal, Rating
from django.contrib.auth.models import User


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id', 'title', 'description', 'no_of_ratings', 'avg_of_ratings']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
       # extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
