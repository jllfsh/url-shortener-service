from django.db import models

from .managers import ClickEventManager


class ClickEvent(models.Model):
    """Model for get some click analytics"""
    count = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    url = models.OneToOneField('shortener.UrlShortener', related_name='click_event')

    objects = ClickEventManager()

    def __str__(self):
        return str(self.count)
