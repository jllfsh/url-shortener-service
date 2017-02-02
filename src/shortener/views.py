from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import View

from .models import UrlShortener


class UrlShortenerDetailView(View):
    """Shows full URL for short URL."""
    @staticmethod
    def get(request, short_url, *args, **kwargs):
        obj = get_object_or_404(UrlShortener, short_url=short_url)
        return HttpResponse('URL: {url}'.format(url=obj.url))
