from rest_framework import generics
from drf_api.permissions import IsOwnerOrReadOnly
from .serializers import DetectoristSerializer
from .models import Detectorist


class DetectoristList(generics.ListAPIView):
    """
    List all detectorists. This endpoint provides a public view of detectorist records.
    """
    queryset = Detectorist.objects.all()
    serializer_class = DetectoristSerializer


class DetectoristDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a detectorist's record. Only the owner has permission to update.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Detectorist.objects.all()
    serializer_class = DetectoristSerializer
