from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    Adds three extra fields when returning a list of Comment instances
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    detectorist_id = serializers.ReadOnlyField(
        source='owner.detectorist.id')
    detectorist_image = serializers.ReadOnlyField(
        source='owner.detectorist.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'detectorist_id', 'detectorist_image',
            'post', 'created_at', 'updated_at', 'content'
        ]