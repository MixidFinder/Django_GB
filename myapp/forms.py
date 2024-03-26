from django import forms


class ProductForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=1000)
    price = forms.DecimalField(max_digits=12, decimal_places=2)
    amount = forms.IntegerField(min_value=1)
    image = forms.ImageField(allow_empty_file=False)
