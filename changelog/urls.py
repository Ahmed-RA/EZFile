from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.alllogs, name='all-logs'),
    path('homepage_view', views.homepage_view, name='homepage_view')
]