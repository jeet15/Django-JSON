from django import forms
from models import Car, User

class CarForm(forms.Form):
    name = forms.CharField(label='Name Of Car', widget = forms.TextInput())
    image = forms.ImageField(label = 'Upload Car Image')

    def save(self):
        data = self.cleaned_data
        car_data = Car(name = data['name'], image= data['image'])
        car_data.save()
        return True

class UserForm(forms.Form):
    name = forms.CharField(label = 'Name' , widget= forms.TextInput())
    email = forms.CharField(label='Email', widget=forms.EmailInput())

    def save(self):
        data = self.cleaned_data
        user_data = User(name = data['name'], email = data['email'])
        user_data.save()
        return True