from django.db import models
from django.db.models.fields import CharField, FloatField, IntegerField
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.models import User

class Place(models.Model):    
    place_name = CharField(max_length=100, null=True)
    place_lat = FloatField(null=True, default=0)
    place_long = FloatField(null=True, default=0)
    place_id = IntegerField(primary_key=True)
<<<<<<< HEAD
    place_exp=CharField(max_length=1000,null=True)
=======
    explain = CharField(max_length=200,null=True)
>>>>>>> origin/master
    def __str__(self) -> str:
        return self.place_name, self.place_exp
    
class QuizLog(models.Model):
    play_time = IntegerField(null=True, default=0)
    point = IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self) -> str:
        return self.user_id
    

# Create your models here.
