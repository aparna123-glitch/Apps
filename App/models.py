from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    usertype=models.CharField(max_length=20)
    
class Student(models.Model):
    student_id=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=200)
    phone_number=models.IntegerField() 

class Teacher(models.Model):
    teacher_id=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=200)
    phone_number=models.IntegerField()
    experience=models.CharField(max_length=20)
    salary=models.IntegerField()