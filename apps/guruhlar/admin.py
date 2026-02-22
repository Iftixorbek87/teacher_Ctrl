from django.contrib import admin
from .models import Guruh


@admin.register(Guruh)
class GuruhAdmin(admin.ModelAdmin):
    list_display = ['nomi', 'patok', 'talabalar_soni', 'jami_vazifalar', 'yaratilgan']
    list_filter = ['patok__oqituvchi', 'patok']
    search_fields = ['nomi', 'patok__nomi']
