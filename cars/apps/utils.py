from django.core.urlresolvers import reverse
from models import Car

from forms import CarForm


class CarList():
    def get_list(self):
        return Car.objects.all().order_by('name')


class ManageCar(object):
    def car_form(self):
        form = CarForm()
        return form

    def save_car(self, request):
        import pdb;pdb.set_trace
        form = CarForm(request.POST)
        if form.is_valid():
            return form.save(request)
        else:
            return False

        
    