from django.core.urlresolvers import reverse
from models import Car

from forms import CarForm


class CarList():
    def get_list(self):
        return Car.objects.all().order_by('name')


#class ManageCar(object):
    