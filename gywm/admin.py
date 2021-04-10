from django.contrib.admin.options import ModelAdmin
from django.contrib import admin
from .models import GYwm, GYwm_GC, GYwm_XX


@admin.register(GYwm)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('gywm_type','created_time')
    ordering = ('gywm_type',)

@admin.register(GYwm_XX)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('name','created_time')
    ordering = ('name',)

@admin.register(GYwm_GC)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('name','created_time')
    ordering = ('name',)
