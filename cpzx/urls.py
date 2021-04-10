from django.urls import path
from . import views


urlpatterns = [
    path('cp_index', views.cp_index),
    path('cp_type_list', views.cp_type_list),
    path('cp_type_detail/<int:cp_type_pk>', views.cp_type_detail),
    path('cp_detail/<int:cp_pk>', views.cp_detail),

]