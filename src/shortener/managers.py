from django.db.models import Manager


class UrlShortenerManager(Manager):
    """
    Custom manager for UrlShorter model.
    """
    def all_active(self):
        return self.filter(active=True)
