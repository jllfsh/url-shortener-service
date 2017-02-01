from django.db.models import Manager

from .utils import make_short_url


class UrlShortenerManager(Manager):
    """
    Custom manager for UrlShorter model.
    """
    def all_active(self):
        return self.get_queryset().filter(active=True)

    def refresh_short_urls(self, items=None):
        urls = self.get_queryset()
        new_urls = 0
        if items and isinstance(items, int):
            urls = urls.order_by('-id')[:items]
        for url in urls:
            url.short_url = make_short_url(url)
            url.save()
            new_urls += 1
        return 'New URLs made {count}'.format(count=new_urls)
