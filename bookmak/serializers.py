from rest_framework import serializers

#from movi.product.models import Movi
from bookmak.models import Bookmark
from product.serializers import ProductListSerializer


class BookmarkListSerializer(serializers.ModelSerializer):

    post = ProductListSerializer()

    class Meta:
        model = Bookmark
        fields = ['post']


class BookmarkCreateSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    # def validate_post(self, post):
    #     user = self.context['request'].user
    #     if (
    #         not post.user.private
    #         or post.user == user
    #         or post.id
    #         in Post.objects.filter(
    #             user_id__in=user.following.values_list('id', flat=True)
    #         ).values_list('id', flat=True)
    #     ):
    #         return post
    #     else:
    #         raise serializers.ValidationError('Not allowed!')

    class Meta:
        model = Bookmark
        fields = '__all__'