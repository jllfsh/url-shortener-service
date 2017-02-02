from django.conf.urls import url
from django.contrib import admin

from shortener.views import UrlShortenerRedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<short_url>[-\w]+)/$', UrlShortenerRedirectView.as_view())
]
