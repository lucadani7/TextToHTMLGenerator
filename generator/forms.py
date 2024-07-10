from django import forms

from generator.models import WebPage


class WebPageForm(forms.ModelForm):
    class Meta:
        model = WebPage
        fields = ['title', 'content', 'background_color', 'text_color']
        widgets = {
            'background_color': forms.TextInput(attrs={'type': 'color'}),
            'text_color': forms.TextInput(attrs={'type': 'color'}),
        }
