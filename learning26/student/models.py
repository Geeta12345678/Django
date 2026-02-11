from django.db import models

# Create your models here
class student(models.Model):
    studentName= models.CharField(max_length=100)
    studentAge= models.IntegerField()
    studentCity= models.CharField(max_length=40)
    studentEmail= models.EmailField(null=True)
       
    class Meta:
        db_table="student"

        def __str__(self):
         return self.studentName

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

    def __str__(self):
        return self.categoryName    


    
class studentprofile(models.Model):
    Hobbies=(("reading","reading"),("traveling","traveling"),("dancing","dancing"))
    studentId=models.OneToOneField(student,on_delete=models.CASCADE)
    studentHobbies=models.CharField(max_length=100,choices=Hobbies)
    studentAddress=models.CharField(max_length=70)
    studentphone=models.CharField(max_length=10)
    studentGender=models.CharField(max_length=10)
    studentDob=models.CharField(max_length=10)
     
    class Meta:
        db_table="studentprofile"

    def __str__(self):
        return self.studentId.studentName    

class Service(models.Model):
    serviceName = models.CharField(max_length=100)
    serviceDescription = models.TextField()
    servicePrice = models.IntegerField()
    serviceStatus = models.BooleanField(default=True)
    #after table creation adding new field
    categoryId = models.ForeignKey(category,on_delete=models.CASCADE)

    class Meta:
        db_table = "service"

    def __str__(self):
        return self.serviceName   
    

class userprofile(models.Model):
   userName=models.CharField(max_length=100)
   userEmail=models.EmailField()
   userPassword=models.CharField(max_length=100)
   userPhone=models.CharField(max_length=10)
   userAddress=models.CharField(max_length=100)

   class Meta:
            db_table="userprofile"
   def __str__(self):
         return self.userName
      

class collage(models.Model):
        collgeName=models.CharField(max_length=100)  
        collageCity=models.CharField(max_length=70)
        collageState=models.CharField(max_length=100)
        class Meta:
            db_table="collage"
        def __str__(self):
          return self.collgeName
        
class department(models.Model):
        departmentName=models.CharField(max_length=100)
        collegeId=models.ForeignKey(collage,on_delete=models.CASCADE)
        class Meta:
            db_table="department"
        def __str__(self):
           return self.departmentName
class subject(models.Model):
        subjectName=models.CharField(max_length=100)
        departmentId=models.ForeignKey(department,on_delete=models.CASCADE)
        class Meta:
            db_table="subject"
        def __str__(self):
           return self.subjectName
         
          
    
   