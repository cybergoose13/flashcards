from django.db import models

# Create your models here.
import bcrypt

class Card(models.Model):
    category= models.CharField(max_length= 32)
    question= models.CharField(max_length= 128)
    answer= models.CharField(max_length= 64)

    created_at= models.DateTimeField(auto_now_add= True)
    updated_at= models.DateTimeField(auto_now= True)