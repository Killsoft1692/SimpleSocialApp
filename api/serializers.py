from rest_framework.serializers import ModelSerializer, SerializerMethodField
from users.models import Profile
from groups.models import Group


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'bio', 'friend_list')

    username = SerializerMethodField()
    friend_list = SerializerMethodField()

    @staticmethod
    def get_username(obj):
        return obj.user.username

    @staticmethod
    def get_friend_list(obj):
        return obj.friends.values('pk', 'username')


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ('name', 'description', 'followers')

    followers = SerializerMethodField()

    @staticmethod
    def get_followers(obj):
        return obj.followers.values('pk', 'username')
