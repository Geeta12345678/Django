from django.db import models

# Create your models here
class student(models.Model):
    studentName= models.CharField(max_length=100)
    studentAge= models.IntegerField()
    studentCity= models.CharField(max_length=40)
    studentEmail= models.EmailField(null=True)
       
    class Meta:
        db_table="student"

class product(models.Model):
    productName=models.CharField(max_length=100)
    productPrice=models.IntegerField()
    productStoke=models.PositiveIntegerField()
    productColor=models.CharField(max_length=70,null=True)
    productStatus=models.BooleanField(default=True)
    productDescription=models.TextField(null=True)

    class Meta:
        db_table="product"

class category(models.Model):
    categoryName=models.CharField(max_length=70)
    categoryStatus=models.BooleanField(default=True)
    
    class Meta:
        db_table="category"
    




