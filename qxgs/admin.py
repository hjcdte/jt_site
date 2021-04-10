from django.contrib.admin.options import ModelAdmin
from django.contrib import admin
from .models import QXgs


@admin.register(QXgs)
class QXgsAdmin(admin.ModelAdmin):
    list_display = ('qxgs_name','created_time')
    ordering = ('qxgs_name',)


