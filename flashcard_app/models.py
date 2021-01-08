from django.db import models

# Create your models here.
import bcrypt

class CardManager(models.Manager):
    def card_validator(self, postData):
        errors= {}
        if len(postData['category']) < 2:
            errors['category']= "Category must contain more than 1 characters."
        if len(postData['question']) < 5:
            errors['question']= "Question must have more than 4 characters."
        if len(postData['answer']) < 1:
            errors['answer']= "Answer must not be empty."
        return errors

class Card(models.Model):
    category= models.CharField(max_length= 32)
    question= models.CharField(max_length= 128)
    answer= models.CharField(max_length= 64)

    created_at= models.DateTimeField(auto_now_add= True)
    updated_at= models.DateTimeField(auto_now= True)

    objects= CardManager()