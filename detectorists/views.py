from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .serializers import DetectoristSerializer
from .models import Detectorist


class DetectoristList(generics.ListAPIView):
    """
    List all detectorists. This endpoint provides a public view of detectorist records.
    """
    queryset = Detectorist.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = DetectoristSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__following__followed__detectorist',
        'owner__followed__owner__detectorist',
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]


class DetectoristDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a detectorist's record. Only the owner has permission to update.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Detectorist.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = DetectoristSerializer
