from django.contrib import admin
from .models import JTNew, IMGNew


@admin.register(JTNew,IMGNew)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','author','published_time','created_time')
    ordering = ('-published_time',)



