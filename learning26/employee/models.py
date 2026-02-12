from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()
    join_date = models.DateField(auto_now_add=True)
    post = models.CharField(max_length=100)

    class Meta:
        db_table = "employee"
        
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    fee = models.IntegerField()
    duration = models.IntegerField()
    class Meta:
        db_table = "course"
    def __str__(self):
        return self.name    

class Staff(models.Model):
    name= models.CharField(max_length=100)  
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    class Meta:
        db_table="staff"
    def __str__(self):
        return self.name 

class Toy(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    category=models.CharField(max_length=100)
    discount=models.CharField(max_length=100)
    class Meta:
        db_table="toy"
    def __str__(self):
        return self.name     

       
    