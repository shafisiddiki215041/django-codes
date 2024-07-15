from django.db import models
from brand_model.models import Brand
from django.contrib.auth.models import User


# Create your models here.
class CarModel(models.Model):
    car_name= models.CharField(max_length=50)
    car_description = models.TextField()
    car_price = models.CharField(max_length=20)
    brand = models.ForeignKey(Brand,on_delete = models.CASCADE)
    quantity = models.IntegerField(default=0)
    image =models.ImageField(upload_to='car_model/media/uploads/',blank =True,null = True)
    
    def reduce_quantity(self):
        if self.quantity >0:
            self.quantity -=1
            self.save()
            
    def __str__(self):
        return self.car_name
    

class Comments(models.Model):
    car = models.ForeignKey(CarModel, on_delete = models.CASCADE, related_name = 'comments')
    name  = models.CharField(max_length=20)
    email = models.EmailField( max_length=254)
    body= models.TextField()
    created_date = models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return f'commented by {self.name}'
    
    
class Buy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.car.car_name
    