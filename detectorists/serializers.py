from rest_framework import serializers
from .models import Detectorist
from followers.models import Follower


class DetectoristSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            # print(following)
            return following.id if following else None
        return None
    

    class Meta:
        model = Detectorist
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'content', 'image', 'best_find', 'is_owner', 'following_id'
        ]