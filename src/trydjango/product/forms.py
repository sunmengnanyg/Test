from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'Title',
            'Event',
            'Feature',
            'Time',
        ]

class PureForm(forms.Form):
    Title = forms.CharField()
    time  = forms.DateTimeField()
    price = forms.DecimalField()
    summary=forms.CharField()


