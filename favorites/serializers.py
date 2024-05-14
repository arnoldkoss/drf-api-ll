from rest_framework import serializers
from django.db import IntegrityError
from .models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    """
    Serializer for the Favorite model.
    Handles the creation of favorites while ensuring unique
    constraints are respected between 'owner' and 'post'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Favorite
        fields = ['id', 'owner', 'post', 'created_at']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'This is already in your wishlist.'
            })