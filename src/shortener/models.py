from django.db import models
from django.urls import reverse

from .managers import UrlShortenerManager
from .utils import make_short_url


class UrlShortener(models.Model):
    """
    Short URL model.
    """
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    short_url = models.CharField(max_length=15, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    url = models.URLField()

    objects = UrlShortenerManager()

    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = make_short_url(self)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('redirect', kwargs={'short_url': self.short_url})
