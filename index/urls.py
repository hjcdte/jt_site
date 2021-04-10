from django.urls import path
from . import views


urlpatterns = [
    path('syimg_index', views.syimg_index),
]