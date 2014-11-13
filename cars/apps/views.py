from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, View, RedirectView
from django.template.loader import render_to_string
from django.middleware.csrf import get_token
#from braces.views import CsrfExemptMixin, JsonRequestResponseMixin

from models import Car
from utils import CarList, ManageCar
import json

from libs.jsonresponse import JSONResponseMixin

class HomeView(TemplateView):

    template_name = 'apps/home.html'

    def get_context_data(self,**kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['menu'] = 'home'
        return context

class APIView(View, JSONResponseMixin, CarList ):

    template_name = 'apps/car.html'

    def get(self, request, *args, **kwargs):
        context = { 'cars': self.get_list() }
        data = {'html': render_to_string(self.template_name, context) }
        data['status'] = 1
        return self.render_to_response(data)

class JhtmlView(TemplateView):

    template_name = 'apps/JHtml.html'

    def get_context_data(self,**kwargs):
        context = super(JhtmlView, self).get_context_data(**kwargs)
        context['menu'] = 'jhtml'
        return context

    def post(self, request, *args, **kwargs):
        data = self.add_user(self.request.POST)
        return self.render_to_response(data)

class CarView(View, JSONResponseMixin , ManageCar):
    template_name = 'apps/add.html'

    def get(self, request, *args, **kwargs):
        data = {}
        form_car = self.car_form()
        context = {'form' : form_car, 'csrf_token_value': get_token(self.request)}
        data['html'] = render_to_string(self.template_name, context)
        return self.render_to_response(data)

 


class JqueryView(TemplateView):

    template_name = 'apps/jquery.html'

    def get_context_data(self,**kwargs):
        context = super(JqueryView, self).get_context_data(**kwargs)
        context['menu'] = 'jquery'
        return context

