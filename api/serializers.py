from rest_framework import serializers
from .models import *



class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class BlItemSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(slug_field='name',read_only=True)
    class Meta:
        model = BlackListItem
        fields = [
            'id',
            'image',
            'name',
            'reason',
            'contact',
            'type',
        ]




class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    # image = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'id',
            'name',
            'name_slug',
            'image',
            'image_post',
            'short_description',
            'text',
            'created_at',
            'tags',
        ]

    # def get_image(self, obj):
    #     return self.context['request'].build_absolute_uri(obj.image.url)





