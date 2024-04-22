from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    detectorist_id = serializers.ReadOnlyField(source='owner.detectorist.id')
    detectorist_image = serializers.ReadOnlyField(source='owner.detectorist.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'detectorist_id',
            'detectorist_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'location', 'era'
        ]