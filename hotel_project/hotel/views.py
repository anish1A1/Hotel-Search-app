from django.shortcuts import render
from .models import *
from django.http import JsonResponse


def get_hotel(request):
    try:
        hotel_obj = Hotel.objects.all()
        
        if request.GET.get('sort_by'):
            sortby_value = request.GET.get('sort_by')
            if sortby_value == 'asc':
                hotel_obj = hotel_obj.order_by('hotel_price')
            elif sortby_value == 'dsc':
                hotel_obj = hotel_obj.order_by('-hotel_price')
            
        if request.GET.get('amount'):
            amount = request.GET.get('amount')
            hotel_obj = hotel_obj.filter(hotel_price__lte = amount)
            
        if request.GET.get('ammenity'):
            amenities = request.GET.get('ammenity')
            amenities = str(amenities).split(',')
            am = []
            for amenitys in amenities:
                am.append(amenitys)
            hotel_obj = hotel_obj.filter(amentities__in = am)
        payload = []
        
        for hotel in hotel_obj:
            payload.append({
                'hotel_name' : hotel.hotel_name,
                'hotel_price': hotel.hotel_price,
                'hotel_description': hotel.hotel_description,
                'banner_image': str(hotel.banner_image),
                'ammenity': hotel.get_ammenity(),
            })
        return JsonResponse(payload, safe= False)
            
    except Exception as e:
        print(e)
    return JsonResponse({'message': 'Something went wrong!!'})
