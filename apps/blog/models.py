from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class BlogCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(
        BlogCategory,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='posts'
    )
    thumbnail = models.ImageField(
        upload_to='blog/thumbnails/'
    )
    content = models.TextField()
    excerpt = models.CharField(max_length=300)
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    reading_time = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title