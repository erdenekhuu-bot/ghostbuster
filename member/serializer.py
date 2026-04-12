from rest_framework import serializers
from .models import Member
from django.contrib.auth.models import User


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Member
        fields = ['user','phone','location','status']

class UserSerializer(serializers.ModelSerializer):
    member = MemberSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['id','username','password','member']
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
