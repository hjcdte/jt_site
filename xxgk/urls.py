from django.urls import path
from . import views

urlpatterns = [
    path('rczp_detail', views.rczp_detail),
    path('jtgg_index', views.jtgg_index),
    path('jtgg_list', views.jtgg_list),
    path('jjgg_detail/<int:jt_pk>', views.jjgg_detail),
]