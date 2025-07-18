from django.urls import path
from . import views

urlpatterns = [
    path('', views.lodging_index, name='lodging_index'),
] 