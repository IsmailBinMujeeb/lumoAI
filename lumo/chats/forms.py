from django import forms
from .models import message


class prompt_form(forms.ModelForm):

    class Meta:
        model = message
        fields = ("text",)
        widgets = {
            "text": forms.Textarea(
                attrs={
                    "class": "w-full transition-all border-none focus:outline-none resize-none max-h-5xl min-h-12 scrollbar-hide",
                    "placeholder": "What can I build today ?",
                    "id": "promptArea",
                    "cols": 0,
                    "rows": 0,
                }
            )
        }
