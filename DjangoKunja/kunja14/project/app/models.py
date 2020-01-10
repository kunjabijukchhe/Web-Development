from django.db import models

# Create your models here.
class User(models.Model):
    First_name=models.CharField(max_length=128)
    Last_name=models.CharField(max_length=128)
    email=models.EmailField(max_length=264,unique=True)

    def __str__(self):
        return self.email

class UserPass(models.Model):
    email=models.ForeignKey(User,on_delete=models.CASCADE)
    password=models.CharField(max_length=128)
