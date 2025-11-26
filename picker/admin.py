

# Register your models here.
from django.contrib import admin
from .models import Map


@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'wg_id', 'layout_type', 'size_m')
    search_fields = ('name_ru', 'wg_id')
    prepopulated_fields = {"slug": ("name_ru",)}
