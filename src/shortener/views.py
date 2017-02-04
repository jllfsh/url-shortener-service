from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import View

from .models import UrlShortener


class HomeView(View):
    """Home page view."""
    @staticmethod
    def get(request, *args, **kwargs):
        return render(request, 'shortener/home.html', {})


class UrlShortenerRedirectView(View):
    """Redirects to full URL for certain short URL."""
    @staticmethod
    def get(request, short_url, *args, **kwargs):
        obj = get_object_or_404(UrlShortener, short_url=short_url)
        return HttpResponseRedirect(obj.url)
