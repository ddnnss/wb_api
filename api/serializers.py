from rest_framework import serializers
from .models import *



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class BlTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'




class BlItemSerializer(serializers.ModelSerializer):
    type = BlTypesSerializer(many=False)
    class Meta:
        model = BlackListItem
        fields = [
            'id',
            'image',
            'name',
            'name_slug',
            'reason',
            'details',
            'proofs',
            'created_at',
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





