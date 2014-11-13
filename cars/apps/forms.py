from django import forms
from models import Car

class CarForm(forms.Form):
    name = forms.CharField(label='Name Of Car', widget = forms.TextInput())
    image = forms.ImageField(label = 'Upload Car Image')

    def save(self):
        data = self.cleaned_data
        car_data = Car(name = data['name'], image= data['image'])
        car_data.save()
        return True
