from django import forms

from customers.models import Customer, Order


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Name'}),
            'admission_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Admission Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Email'}),
            'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Gender'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Age'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control',
                                                     'accept': 'images/*',
                                                     'title':'upload your image here'})
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Price'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Quantity'}),
        }
