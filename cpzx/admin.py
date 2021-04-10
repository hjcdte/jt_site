from django.contrib.admin.options import ModelAdmin
from django.contrib import admin
from .models import Cp, Cp_Type


@admin.register(Cp)
class CpyFwAdmin(admin.ModelAdmin):
    list_display = ('option','cp_name','cp_type','created_time')
    ordering = ('-option','cp_type','cp_name')


@admin.register(Cp_Type)
class CpyFw_TypeAdmin(admin.ModelAdmin):
    list_display = ('cp_type','created_time')
    ordering = ('cp_type',)
