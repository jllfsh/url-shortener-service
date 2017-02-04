from django.conf.urls import url
from django.contrib import admin

from shortener.views import HomeView, UrlShortenerRedirectView

urlpatterns = [
    url(r'^$', HomeView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<short_url>[-\w]+)/$', UrlShortenerRedirectView.as_view())
]
