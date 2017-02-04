from django import forms

from .models import UrlShortener


class CreateURLFrom(forms.ModelForm):
    """Form for create a new UrlShortener instance."""
    class Meta:
        model = UrlShortener
        fields = ('url',)
