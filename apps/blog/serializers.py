from rest_framework import serializers
from .models import (
    BlogCategory,
    Tag,
    BlogPost
)

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer(read_only=True)
    tags = TagSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = BlogPost
        fields = '__all__'