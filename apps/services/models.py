from django.db import models
from django.utils.text import slugify


class Service(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True,
        blank=True
    )
    short_description = models.CharField(max_length=300)
    description = models.TextField()
    icon = models.ImageField(
        upload_to='services/icons/'
    )
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        
    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title