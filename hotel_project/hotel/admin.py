from django.contrib import admin
from .models import *


class HotelAmin(admin.ModelAdmin):
    list_display = ['hotel_name', 'hotel_price', 'hotel_description']

admin.site.register(Amenities)
admin.site.register(Hotel)
admin.site.register(HotelImage)



# Register your models here.
