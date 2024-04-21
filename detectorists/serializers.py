from rest_framework import serializers
from .models import Detectorist


class DetectoristSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Detectorist
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'content', 'image', 'best_find'
        ]