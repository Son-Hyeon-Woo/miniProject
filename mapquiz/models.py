from django.db import models
from django.db.models.fields import CharField, FloatField, IntegerField

class Place(models.Model):
    
    place_name = CharField(max_length=100, null=True)
    place_lat = FloatField(null=True, default=0)
    place_long = FloatField(null=True, default=0)
    place_id = IntegerField(primary_key=True)
    
    def __str__(self) -> str:
        return self.place_name
    
    class Meta:
        db_table = 'place'
        app_label = 'mapquiz'
        managed = False

# Create your models here.
