from django.urls import path, include
from . import views


app_name = 'buybooks'

urlpatterns = [
    path('', views.home, name='home'),

]