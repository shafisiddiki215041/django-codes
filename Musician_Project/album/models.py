from django.db import models
from musician.models import MusicianDetails

class AlbumEntry(models.Model):
    album_name = models.CharField(max_length=100)
    musician = models.ForeignKey(MusicianDetails,on_delete = models.CASCADE)
    Release_date= models.DateField()
    ratings = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ]
    rating = models.CharField(choices=ratings, max_length=5)
    
    def __str__(self):
        return self.album_name