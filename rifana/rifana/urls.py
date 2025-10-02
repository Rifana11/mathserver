from django.urls import path
from . import views 

urlpatterns = [
    path('', views.power_calculator, name='power_calculator_root'),
    path('power/', views.power_calculator, name='power_calculator'),

]