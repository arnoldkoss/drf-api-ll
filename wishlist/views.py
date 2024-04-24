from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Wishlist
from .serializers import WishlistSerializer


class WishlistList(generics.ListCreateAPIView):
    """
    Provides a list and creation view for wishlist items.
    GET requests return a list of all wishlist items.
    POST requests allow authenticated users to add a new 
    item to their wishlist,
    associating it with the logged-in user.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = WishlistSerializer
    queryset = Wishlist.objects.all()   

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class WishlistDetail(generics.RetrieveDestroyAPIView):
    """
    Provides a detail view for a specific wishlist item.
    GET requests retrieve the details of a specific 
    wishlist item.
    DELETE requests allow the owner of the wishlist 
    item to remove it from the database.
    Ensures that only the owner can delete the item, 
    aligning with the IsOwnerOrReadOnly permission.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = WishlistSerializer
    queryset = Wishlist.objects.all()