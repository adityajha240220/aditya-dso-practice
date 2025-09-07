from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from tinymce.models import HTMLField

class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = HTMLField()
    category = models.CharField(max_length=100, default="General")
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
