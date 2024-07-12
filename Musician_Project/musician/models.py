from django.db import models

from datetime import date

class MusicianDetails(models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Email=models.EmailField()
    Phone_No= models.CharField(max_length=100)
    instrument_type =[
        ('drum', 'drum'),
        ('pianno', 'pianno'),
        ('harmony', 'harmony'),
    ]
    favo_instrument= models.CharField(max_length=10,choices=instrument_type)
    
    def __str__(self):
        return self.First_name
