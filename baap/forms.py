from django import forms
from tinymce.widgets import TinyMCE
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ["title", "content", "category"]
        widgets = {
            "content": TinyMCE(),
        }
