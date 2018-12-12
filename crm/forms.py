from django import forms
from .models import Customer, Service, Product


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('cust_name', 'organization', 'role', 'bldgroom', 'account_number', 'address', 'city', 'state',
                  'zipcode', 'email')


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('category', 'name', 'author', 'image', 'edition', 'isbn', 'price', 'sellername', 'selleremail',
                  'sellerphone')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('cust_name', 'product', 'p_description', 'quantity', 'pickup_time', 'charge')


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)
