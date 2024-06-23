from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(ImageLogin)
class OptionImpressionAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = [field.name for field in ImageLogin._meta.fields ]
