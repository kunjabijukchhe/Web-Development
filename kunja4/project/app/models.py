from django.db import models

# Create your models here.
class Record(models.Model):
    name=models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.name
class Website(models.Model):
    name=models.ForeignKey(Record,on_delete=models.CASCADE)
    webName=models.CharField(max_length=264,unique=True)
    url=models.URLField(unique=True)

    def __str__(self):
        return self.webName
