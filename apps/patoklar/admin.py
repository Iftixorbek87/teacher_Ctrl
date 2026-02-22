from django.contrib import admin
from .models import Patok


@admin.register(Patok)
class PatokAdmin(admin.ModelAdmin):
    list_display = ['nomi', 'oqituvchi', 'guruhlar_soni', 'talabalar_soni', 'yaratilgan']
    list_filter = ['oqituvchi']
    search_fields = ['nomi']
