from rest_framework import serializers
from django.db import IntegrityError
from .models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    """
    Serializer for the Favorite model.
    Handles the creation of favorites while ensuring unique
    constraints are respected between 'owner' and 'post',
    and 'owner' and 'detectorist'.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Favorite
        fields = ['id', 'owner', 'post', 'detectorist', 'created_at']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })