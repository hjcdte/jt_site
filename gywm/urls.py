from django.urls import path
from . import views

urlpatterns = [
    path('gywm/<str:type_name>', views.gywm_list),
    path('jtgc_list', views.jtgc_list),
    path('ppxx_list', views.ppxx_list),
]