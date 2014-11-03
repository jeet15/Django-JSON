from django.core.urlresolvers import reverse
from models import Car


class CarList():
    def get_list(self):
        return Car.objects.all().order_by('name')
