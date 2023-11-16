from django.db import models
from django.contrib.auth.models import User,auth

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    

    def  __str__(self):
      return self.name
    


class Type(models.Model):
    name=models.CharField(max_length=50)
    

    def  __str__(self):
      return self.name




class product(models.Model): 
   
   name=models.CharField(max_length=100)
   desc=models.CharField(max_length=500)  
   
   image1=models.ImageField(upload_to="uploads")
   image2=models.ImageField(upload_to="uploads")
   image3=models.ImageField(upload_to="uploads")
   price=models.IntegerField(default=0)  
   category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1) 
   type=models.ForeignKey(Type,on_delete=models.CASCADE,default=1)   
   def  __str__(self):
      return self.name 


class cart(models.Model):
   name=models.CharField(max_length=100)
   image=models.ImageField(upload_to="uploads") 
   price=models.IntegerField(default=0)
   
   totalprice=models.IntegerField(default=0) 
   qty=models.IntegerField(default=0) 
   username=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
   
  
   def  __str__(self):
      return str(self.name)     
