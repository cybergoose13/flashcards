from django.db import models

# Create your models here.
import bcrypt

class Card(models.Model):
    catagory= models.CharField(max_length= 32)
    question= models.CharField(max_length= 128)
    answer= models.CharField(max_length= 64)
    wrong_one= models.CharField(max_length= 64)
    wrong_two= models.CharField(max_length= 64)
    wrong_three= models.CharField(max_length= 64)

    created_by= models.CharField(max_length= 16)

    created_at= models.DateTimeField(auto_now_add= True)
    updated_at= models.DateTimeField(auto_now= True)