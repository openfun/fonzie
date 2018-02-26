from rest_framework.serializers import ModelSerializer

from .models import UserProfile


class UserProfileSerializer(ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('user', 'name')
        depth = 2
