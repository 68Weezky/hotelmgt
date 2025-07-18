from django.urls import path
from . import views

urlpatterns = [
    path('', views.conference_index, name='conference_index'),
] 