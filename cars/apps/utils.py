from django.core.urlresolvers import reverse
from models import Car

from forms import CarForm, UserForm


class CarList():
    def get_list(self):
        return Car.objects.all().order_by('name')


class ManageCar(object):
    def car_form(self):
        form = CarForm()
        return form



class ManageUser(object):
    def get_form(self):
        form = UserForm()
        return form
    
    def save_form(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            return form.save(request)
        else:
            return False