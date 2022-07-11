from .models import Link
from django import forms


class AddForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['author', 'link',]