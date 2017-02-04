from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, View

from .forms import CreateURLFrom
from .models import UrlShortener


class HomeView(CreateView):
    """Home page view."""
    template_name = 'shortener/home.html'
    form_class = CreateURLFrom

    def form_valid(self, form):
        super().form_valid(form)
        return render(self.request, self.template_name, context={
            'form': form,
            'short_url': self.request.build_absolute_uri(self.object.get_absolute_url())
        })


class UrlShortenerRedirectView(View):
    """Redirects to full URL for certain short URL."""
    @staticmethod
    def get(request, short_url, *args, **kwargs):
        obj = get_object_or_404(UrlShortener, short_url=short_url)
        return HttpResponseRedirect(obj.url)
