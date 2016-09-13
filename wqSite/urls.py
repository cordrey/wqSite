"""wqSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
#from graph.views import index, detail, current_datetime
from graph.views import index, chart_data_json, LevelChartsView, record_detail

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^$', chart_data_json),
    url(r'(^\d{4}-\d{2}-\d{2} \d{2}:\d{2})/$', record_detail),  #changing space to _ results in validation error
    #url(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})/$', record_detail),
    url(
        regex=r'^graph/$',
        view=LevelChartsView.as_view(),
        name='water_level',
    ),
    #url(r'^([\d]+)/$', current_datetime),
]
