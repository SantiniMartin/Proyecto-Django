from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    dni = models.IntegerField(null=True)
    
    class Meta:
        db_table = 'usuario'
        
    def __str__(self):
        return f"{self.id} - {self.username}. {self.first_name} - {self.last_name}"