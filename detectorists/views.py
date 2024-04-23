from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Detectorist
from .serializers import DetectoristSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class DetectoristList(APIView):
    def get(self, request):
        detectorists = Detectorist.objects.all()
        serializer = DetectoristSerializer(
            detectorists, many=True, context={'request': request})
        return Response(serializer.data)


class DetectoristDetail(APIView):
    serializer_class = DetectoristSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            detectorist = Detectorist.objects.get(pk=pk)
            self.check_object_permissions(self.request, detectorist)
            return detectorist
        except Detectorist.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        detectorist = self.get_object(pk)
        serializer = DetectoristSerializer(
            detectorist, context={'request': request}
            )
        return Response(serializer.data)
    
    def put(self, request, pk):
        detectorist = self.get_object(pk)
        serializer = DetectoristSerializer(
            detectorist, data=request.data, context={'request': request}
            )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)