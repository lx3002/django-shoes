from django import forms
from shoe.models import shoes


class shoeform(forms.ModelForm):
    class Meta:
        model = shoes
        fields = "__all__"
