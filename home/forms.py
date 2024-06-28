from django import forms
from .models import Update
from pictures.widgets import CustomClearableFileInput


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Update
        fields = ('heading_update',)
        widgets = {
            'heading_update': forms.Textarea(attrs={'class': 'form-control'}),
        }
