from django.contrib import admin
from .models import (
    BlogCategory,
    Tag,
    BlogPost
)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'is_featured',
        'is_published',
        'created_at'
    )
    list_filter = (
        'category',
        'is_featured',
        'is_published'
    )
    search_fields = (
        'title',
        'content',
        'excerpt'
    )
    prepopulated_fields = {
        'slug': ('title',)
    }

admin.site.register(BlogCategory)
admin.site.register(Tag)