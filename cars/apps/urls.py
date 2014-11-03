from django.conf.urls import patterns, url

from views import HomeView, APIView

urlpatterns = patterns("apps",
    url(r'^$',HomeView.as_view(),name='home'),
    url(r'^get-list/$',APIView.as_view(),name='get_list'),
    )