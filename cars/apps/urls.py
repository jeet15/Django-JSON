from django.conf.urls import patterns, url

from views import HomeView, APIView, JqueryView, JhtmlView, CarView, SampleView

urlpatterns = patterns("apps",
    url(r'^$',HomeView.as_view(),name='home'),
    url(r'^get-list/$',APIView.as_view(),name='get_list'),
    url(r'^jquery/$',JqueryView.as_view(),name='jquery'),
    url(r'^jhtml/$',JhtmlView.as_view(),name='jhtml'),
    url(r'^add-car/$',CarView.as_view(),name='add-car'),
    url(r'^sample/$',SampleView.as_view(),name='sample'),
    )