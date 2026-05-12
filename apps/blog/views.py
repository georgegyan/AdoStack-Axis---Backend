from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostListView(generics.ListAPIView):
    queryset = BlogPost.objects.filter(is_published=True)
    serializer_class = BlogPostSerializer
    filterset_fields = [
        'category',
        'is_featured'
    ]
    search_fields = [
        'title',
        'content',
        'excerpt'
    ]
    ordering_fields = [
        'created_at'
    ]

class BlogPostDetailView(generics.RetrieveAPIView):
    queryset = BlogPost.objects.filter(is_published=True)
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'