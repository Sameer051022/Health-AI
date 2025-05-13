from rest_framework import serializers
from .models import User, Session

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'medical_records', 'profile_pic']

class SessionSerializer(serializers.ModelSerializer):
    user_email = serializers.CharField(write_only=True)  # Accept email instead of ID
    class Meta:
        model = Session
        fields = ['id', 'user_email', 'session_chats', 'created_at', 'updated_at']
