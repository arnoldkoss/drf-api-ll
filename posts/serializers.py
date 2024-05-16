from rest_framework import serializers
from posts.models import Post
from likes.models import Like
from wishlist.models import Wishlist
from favorites.models import Favorite


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(
        source='owner.username')
    is_owner = serializers.SerializerMethodField()
    detectorist_id = serializers.ReadOnlyField(
        source='owner.detectorist.id')
    detectorist_image = serializers.ReadOnlyField(
        source='owner.detectorist.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    wishlist_id = serializers.SerializerMethodField()
    wishlists_count = serializers.ReadOnlyField()
    favorite_id = serializers.SerializerMethodField()
    favorites_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    def get_wishlist_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            wishlist = Wishlist.objects.filter(
                owner=user, post=obj
            ).first()
            return wishlist.id if wishlist else None
        return None

    def get_favorite_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            favorite = Favorite.objects.filter(
                owner=user,
            ).first()
            return favorite.id if favorite else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'detectorist_id',
            'detectorist_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'location', 'era',
            'like_id', 'likes_count', 'comments_count',
            'wishlists_count', 'wishlist_id', 'favorites_count',
            'favorite_id'
        ]
