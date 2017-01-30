from django.db import models


class UrlShortener(models.Model):

    url = models.CharField(max_length=255)

    def __str__(self):
        return self.url
