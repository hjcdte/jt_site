from django.contrib.admin.options import ModelAdmin
from django.contrib import admin
from .models import XXgk_RC, XXgk_GG


@admin.register(XXgk_RC)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('published_time','created_time',)
    ordering = ('-published_time',)

@admin.register(XXgk_GG)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','published_time','created_time',)
    ordering = ('-published_time',)