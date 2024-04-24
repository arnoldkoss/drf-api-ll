from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Favorite
from .serializers import FavoriteSerializer


class FavoriteList(generics.ListCreateAPIView):
    """
    Provides a list of all favorite items and 
    allows creation of new favorites.
    
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()   

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FavoriteDetail(generics.RetrieveDestroyAPIView):
    """
    Provides methods to retrieve and delete a
    specific favorite item.
    The view uses the IsOwnerOrReadOnly permission
    to restrict deletion capabilities
    to just the owner of the favorite.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()