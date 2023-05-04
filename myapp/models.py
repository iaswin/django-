from django.db import models

# Create your models here.
class Teacher(models.Model):
    FirstName=models.CharField(max_length=10)
    LastName=models.CharField(max_length=10)
    Email=models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.FirstName
    
class Users(models.Model):
    FirstName=models.CharField(max_length=10)
    LastName=models.CharField(max_length=10)
    Email=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
    
class imagges(models.Model):
    image=models.ImageField(upload_to="img/")
    
    
    
    

    
    
    