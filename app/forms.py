from django import forms
from .models import Registered

class Registered(forms.ModelForm):
    class Meta:
        model = Registered
        fields = "__all__"

#Registration DB