from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers

# Custom serializer for user details.
# This serializer extends the UserDetailsSerializer from
# 'dj_rest_auth' to include 'detectorist_id' and 'detectorist_image' fields.
# These additional fields are read-only and sourced from the
# related 'detectorist' object.

class CurrentUserSerializer(UserDetailsSerializer):
    detectorist_id = serializers.ReadOnlyField(source='detectorist.id')
    detectorist_image = serializers.ReadOnlyField(source='detectorist.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'detectorist_id', 'detectorist_image'
        )