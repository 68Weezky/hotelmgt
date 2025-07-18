from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff_index, name='staff_index'),
] 