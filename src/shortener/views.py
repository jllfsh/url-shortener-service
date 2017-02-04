from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, RedirectView

from .models import UrlShortener


class HomeView(CreateView):
    """Home page view."""
    template_name = 'shortener/home.html'
    model = UrlShortener
    fields = ('url',)

    def form_valid(self, form):
        super().form_valid(form)
        context = {
            'form': form,
            'short_url': self.request.build_absolute_uri(self.object.get_absolute_url())
        }
        return render(self.request, self.template_name, context)


class UrlShortenerRedirectView(RedirectView):
    """Redirects to full URL for certain short URL."""
    def get_redirect_url(self, short_url, *args, **kwargs):
        url_object = get_object_or_404(UrlShortener, short_url=short_url)
        return url_object.url
