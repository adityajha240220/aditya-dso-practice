from django.contrib.auth.models import AbstractUser
from django.db import models


# Write the code for a simple Django model Student with fields name, age, and email.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.name

# Show the code to extend Django’s default User model using AbstractUser.  

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username        
