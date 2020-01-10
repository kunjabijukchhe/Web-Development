from django.db import models

# Create your models here.
class User(models.Model):
    First_Name=models.CharField(max_length=264)
    Last_Name=models.CharField(max_length=264)
    email=models.EmailField(max_length=264,unique=True)


    def __str__(self):
        return self.email

class Website(models.Model):
    email=models.ForeignKey(User,on_delete=models.CASCADE)
    password=models.CharField(max_length=10,unique=True)
