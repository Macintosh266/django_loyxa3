from django import forms
from .models import product, costumer, orders

class ProductForm(forms.ModelForm):
    class Meta:
        model = product
        fields = ['name', 'price', 'valid_time']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'price': forms.NumberInput(attrs={"class": "form-control"}),
            'valid_time': forms.DateTimeInput(attrs={
                "class": "form-control",
                "type": "datetime-local"
            }),
        }
        labels = {
            'name': 'Product Name',
            'price': 'Price',
            'valid_time': 'Valid Time',
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = orders
        fields = ['name','product', 'costumer', 'quantity', 'requared_date', 'shipped_date']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'product': forms.Select(attrs={"class": "form-control"}),
            'costumer': forms.Select(attrs={"class": "form-control"}),
            'quantity': forms.NumberInput(attrs={"class": "form-control"}),
            'requared_date': forms.DateTimeInput(attrs={
                "class": "form-control",
                "type": "datetime-local"
            }),
            'shipped_date': forms.DateTimeInput(attrs={
                "class": "form-control",
                "type": "datetime-local"
            }),
        }
        labels = {
            'product': 'Product',
            'costumer': 'Customer',
            'quantity': 'Quantity',
            'requared_date': 'Required Date',
            'shipped_date': 'Shipped Date',
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = costumer
        fields = ['name', 'addres', 'email']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'addres': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
        }
        labels = {
            'name': 'Customer Name',
            'addres': 'Address',
            'email': 'Email',
        }
