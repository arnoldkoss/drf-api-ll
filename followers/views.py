from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


class FollowerList(generics.ListCreateAPIView):
    """
    Provides a list of all Follower instances and allows
    for creating a new follow relationship.
    Only authenticated users can create a new follow relationship.
    The list of followers
    can be viewed by any user, whether authenticated or not.

    The perform_create method is overridden to automatically
    set the 'owner' of a new
    Follower instance to the currently authenticated user,
    ensuring that users can only
    create follow relationships where they are the owner.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a follower
    No Update view, as we either follow or unfollow users
    Destroy a follower, i.e. unfollow someone if owner
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    