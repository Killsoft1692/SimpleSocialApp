from .serializers import ProfileSerializer, GroupSerializer
from rest_framework.generics import ListAPIView
from users.models import Profile
from groups.models import Group


class ProfileListView(ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class GroupListView(ListAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
