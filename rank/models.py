from django.db import models
from django.contrib.auth.models import User

class Around_place(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    id_p=models.IntegerField()
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'around_place'
        app_label = 'rank'
        managed = False
      
      
        
# class Point(models.Model):
#     point = models.IntegerField(default=0)
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     def __str__(self) -> str:
#         return self.user_id
# Create your models here.
