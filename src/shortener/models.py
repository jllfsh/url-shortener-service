from django.db import models


class UrlShortener(models.Model):

    url = models.CharField(max_length=255)
    short_url = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.url
