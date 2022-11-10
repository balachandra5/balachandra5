from django.db import models

# Create your models here.
class employee(models.Model):
    ename=models.CharField(max_length=62)
    eno=models.IntegerField()
    eid=models.IntegerField() 
    
class book(models.Model):
  num=models.IntegerField()
  bid=models.IntegerField()
  bname=models.CharField(max_length=77)
   