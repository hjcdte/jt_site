from django.urls import path
from . import views

urlpatterns = [
    path('qxgs_list', views.qxgs_list),
    path('qxgs_detail/<int:name_id>', views.qxgs_detail),
]