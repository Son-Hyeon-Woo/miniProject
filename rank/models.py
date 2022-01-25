from django.db import models

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
# Create your models here.
