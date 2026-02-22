from django.contrib import admin
from .models import Talaba, VazifaBajarish


@admin.register(Talaba)
class TalabaAdmin(admin.ModelAdmin):
    list_display = ['ism_familya', 'guruh', 'bajarilgan_soni', 'foiz', 'bitirdimi']
    list_filter = ['guruh__patok', 'guruh']
    search_fields = ['ism_familya']

    def bitirdimi(self, obj):
        return obj.bitirdimi()
    bitirdimi.boolean = True
    bitirdimi.short_description = "Bitirdi"


@admin.register(VazifaBajarish)
class VazifaBajarishAdmin(admin.ModelAdmin):
    list_display = ['talaba', 'vazifa_raqam', 'bajarildi', 'vaqt']
    list_filter = ['bajarildi', 'talaba__guruh']
    search_fields = ['talaba__ism_familya']
