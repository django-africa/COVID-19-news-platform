from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('test/', views.covid19_country, name='country'),
    path('register/', views.register, name='register')

]