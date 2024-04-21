from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Detectorist
from .serializers import DetectoristSerializer


class DetectoristList(APIView):
    def get(self, request):
        detectorists = Detectorist.objects.all()
        serializer = DetectoristSerializer(detectorists, many=True)
        return Response(serializer.data)
