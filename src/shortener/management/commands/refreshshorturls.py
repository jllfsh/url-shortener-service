from django.core.management.base import BaseCommand

from shortener.models import UrlShortener


class Command(BaseCommand):
    help = 'Refresh all short URLs'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        return UrlShortener.objects.refresh_short_urls(items=options['items'])
