from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DetailView, RedirectView

from .forms import CreateURLFrom
from .models import UrlShortener
from analytics.models import ClickEvent


class HomeView(CreateView):
    """Home page view."""
    form_class = CreateURLFrom
    template_name = 'shortener/home.html'

    def get_success_url(self):
        return reverse('detail', kwargs={'short_url': self.object.short_url})


class UrlDetailView(DetailView):
    """Shows created short URL details."""
    model = UrlShortener
    slug_field = 'short_url'
    slug_url_kwarg = 'short_url'
    template_name = 'shortener/detail.html'
    context_object_name = 'url_object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['absolute_short_url'] = self.request.build_absolute_uri(self.object.get_absolute_url())
        return context
    

class UrlShortenerRedirectView(RedirectView):
    """Redirects to full URL for certain short URL."""
    def get_redirect_url(self, short_url, *args, **kwargs):
        url_object = get_object_or_404(UrlShortener, short_url=short_url)
        ClickEvent.objects.create_click_event(url_object)
        return url_object.url
