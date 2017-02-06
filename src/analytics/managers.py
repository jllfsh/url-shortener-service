from django.db import models

from shortener.models import UrlShortener


class ClickEventManager(models.Manager):

    def create_click_event(self, instance):
        if isinstance(instance, UrlShortener):
            obj, created = self.get_or_create(url=instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None
