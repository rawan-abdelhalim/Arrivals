from django.conf.urls import url
from django.views.generic import TemplateView

from main.views import (InternCreate, LateCreate, InternDetailView, LateDetailView, InternListView, InternDelete)

urlpatterns = [
url('^$', TemplateView.as_view(template_name="main/home.html"),
        name="home"),
url(r'^intern/$', InternCreate.as_view(), name="intern_form"),
url(r'^late/$', LateCreate.as_view(), name="late_form"),
url(r'^intern/(?P<pk>\d+)/$', InternDetailView.as_view(), name="intern_detail"),
url(r'^late/(?P<pk>\d+)/$', LateDetailView.as_view(), name="late_detail"),
url(r'^interns/list/$', InternListView.as_view(), name="intern_list"),
url(r'^intern/delete/(?P<pk>\d+)/$', InternDelete.as_view(), name="intern_delete"),


]