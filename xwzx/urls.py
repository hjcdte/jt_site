from django.urls import path
from . import views


urlpatterns = [
    path('jtnew_index', views.jtnew_index),
    path('jtnew_list', views.jtnew_list),
    path('jtnew_detail/<int:JTNew_pk>', views.jtnew_detail),

    path('imgnew_index', views.imgnew_index),
    path('imgnew_list', views.imgnew_list),
    path('imgnew_detail/<int:IMGNew_pk>', views.imgnew_detail),
]