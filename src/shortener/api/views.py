from django.http.response import HttpResponse
from django.views.generic import View


class ApiFeatureView(View):
    """Shows info about API feature"""
    @staticmethod
    def get(request, *args, **kwargs):
        return HttpResponse('Some information about API')
