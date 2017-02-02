from django.conf.urls import url

from .views import ApiFeatureView

urlpatterns = [
    url(r'', ApiFeatureView.as_view())
]
