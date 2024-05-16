from rest_framework import serializers
from django.db import IntegrityError
from .models import Wishlist


class WishlistSerializer(serializers.ModelSerializer):
    """
        Creates a new Wishlist instance while handling the unique
        constraint on 'owner' and 'post'.

        If the unique constraint is violated (i.e., the user has
        already added the post to their wishlist),
        this method raises a ValidationError with a custom message
        indicating a duplicate entry.
        """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Wishlist
        fields = ['id', 'created_at', 'owner', 'post']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'This is already in your wishlist.'
            })
