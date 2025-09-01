from django.db import models

class Amenities(models.Model):
    amenity = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.amenity

# Create your models here.
class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_price = models.IntegerField()
    amentities = models.ManyToManyField(Amenities)
    banner_image = models.ImageField(upload_to='hotels')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hotel_description = models.TextField()
    
    def get_ammenity(self):
        payload = []
        
        for amenitys in self.amentities.all():
            payload.append({'id': amenitys.id, 'amenity': amenitys.amenity})
        return payload
    def __str__(self):
        return self.hotel_name
    
        

class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='hotels')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.hotel.hotel_name
    