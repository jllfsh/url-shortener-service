from django.db import models


class UrlShortener(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    short_url = models.CharField(max_length=15, unique=True)
    updated = models.DateTimeField(auto_now=True)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.url
