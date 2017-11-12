"""hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include, url, patterns
from django.contrib import admin
from hospital_management import views
from django.conf.urls.defaults import patterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.userLogin, name='login'),
    url(r'^login/$', views.userLogin, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^(?P<username>\w+)/profile/$', views.profile, name='profile'),
    url(r'^(?P<username>\w+)/staffProfile/$', views.staffProfile, name='staffProfile'),
    url(r'^(?P<username>\w+)/staffProfile/(?P<patient>\w+)$', views.updateUser, name='updateUser'),
    url(r'^logout/$', views.userLogout, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profileEdit/$', views.profileEdit, name='profileEdit'),
    url(r'^createAppForm/', views.createApp, name='createAppForm'),
    url(r'^deleteAppForm/(\d+)$', views.deleteApp, name='deleteAppForm'),
    url(r'^export/$', views.export, name='export')
]