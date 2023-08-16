from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.managers import UserManager

# Create your models here.
GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('not to disclose', 'Not To Disclose'))

class User(AbstractUser):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=15)
    phonenumber = models.CharField(max_length=12)
    role = models.CharField(max_length=10)
    
    #adress
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    
    def __str__(self):
        return self.get_full_name()
    
    objects = UserManager()
    