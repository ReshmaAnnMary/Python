from django import forms
from .models import TODO


class Form(forms.ModelForm):
    class Meta:
        model = TODO
        fields = ['task', 'priority', 'date']
