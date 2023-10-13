from .models import date
from django import forms
class todoform(forms.ModelForm):
    class Meta:
        model=date
        fields=['name','priority','date']