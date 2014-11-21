from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, View, RedirectView
from django.template.loader import render_to_string
from django.middleware.csrf import get_token
#from braces.views import CsrfExemptMixin, JsonRequestResponseMixin

from models import Car
from utils import CarList, ManageCar, ManageUser 
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

class JhtmlView(TemplateView, ManageCar):

    template_name = 'apps/JHtml.html'

    def get_context_data(self,**kwargs):
        context = super(JhtmlView, self).get_context_data(**kwargs)
        context['menu'] = 'jhtml'
        return context


class CarView(View, JSONResponseMixin , ManageCar):
    template_name = 'apps/add.html'

    def get(self, request, *args, **kwargs):
        data = {}
        form_car = self.car_form()
        context = {'action':'add','form' : form_car, 'csrf_token_value': get_token(self.request)}
        data['html'] = render_to_string(self.template_name, context)
        return self.render_to_response(data)

class SampleView(TemplateView):
    template_name = 'apps/sample.html'

    def get_context_data(self, **kwargs):
        context = super(SampleView, self). get_context_data(**kwargs)
        context['menu'] = 'sample'
        return context
 
class ValidationView(TemplateView):
    template_name = 'apps/jvalid.html'

    def get_context_data(self,**kwargs):
        context = super(ValidationView, self).get_context_data(**kwargs)
        context['menu'] = 'jhtml'
        return context


class UserView(View, JSONResponseMixin, ManageUser):
    template_name = 'apps/user.html'

    def get(self, request, *args, **kwargs):
        data = {}
        user_form = self.get_form()
        context = {'form' : user_form, 'csrf_token_value':get_token(self.request)}
        data['html'] = render_to_string(self.template_name, context)
        return self.render_to_response(data)

    def post(self, request, *args, **kwargs):
        data = {}
        dt = self.save_form(self.request)
        if dt:
            data['status'] = 1
            data['message'] = "user added succesfully..."
        else:
            data['status'] = 0
            data['message'] = "data s missing"
        return self.render_to_response(data)

class JqueryView(TemplateView):

    template_name = 'apps/jquery.html'

    def get_context_data(self,**kwargs):
        context = super(JqueryView, self).get_context_data(**kwargs)
        context['menu'] = 'jquery'
        return context

class UserListView(View, JSONResponseMixin, ManageUser):
    template_name = 'apps/alluser.html'

    def get(self, request, *args, **kwargs):
        context = { 'users': self.get_list() }
        data = {'html': render_to_string(self.template_name, context) }
        data['status'] = 1
        return self.render_to_response(data)

class EditView(View, JSONResponseMixin, ManageUser):

    template_name = 'apps/add.html'

    def get(self, request, *args, **kwargs):
        data = {}
        user_id = self.request.GET.get('user_id')
        edit_form = self.edit_user(user_id)
        context = {'action':'edit','form' : edit_form, 'csrf_token_value': get_token(self.request)}
        data['status'] = 1
        data['html'] = render_to_string(self.template_name, context)
        return self.render_to_response(data)  
              
class DeleteView(View, JSONResponseMixin, ManageUser):
    '''
    @summary: Delete User
    '''
    def get(self, request, *args, **kwargs):
        user_id = self.request.GET.get('user_id')
        data = self.delete_user(user_id)
        return self.render_to_response(data)
