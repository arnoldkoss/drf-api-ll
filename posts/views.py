from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
        wishlists_count=Count('wishlist', distinct=True),
        favorites_count=Count('favorites', distinct=True),

    ).order_by('-created_at')

    # Define filter backends for ordering, searching and filtering
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    # Define fields for filtering
    filterset_fields = [
        'owner__followed__owner__detectorist',
        'likes__owner__detectorist',
        'owner__detectorist',
        'wishlist__owner__detectorist',
        'favorites__owner__detectorist',


    ]
    search_fields = [
        'owner__username',
        'title',
    ]

    # Define fields for ordering
    ordering_fields = [
        'likes_count',
        'comments_count',
        'wishlists_count',
        'favorites_count',
        'likes__created_at',
        'wishlists__created_at',
        'favorites__created_at',

    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
        wishlists_count=Count('wishlist', distinct=True),
        favorites_count=Count('favorites', distinct=True),

    ).order_by('-created_at')
