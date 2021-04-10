from django.contrib import admin
from .models import SYImg


@admin.register(SYImg)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('published_time','created_time')
    ordering = ('-published_time',)