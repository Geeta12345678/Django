from django import forms
from .models import Employee,Course,Staff,Toy

#employee form
#modelForm -->it will create form using model fileds
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__' #[name,age,salary,joiningDate,post]

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__' 

class StaffForm(forms.ModelForm):
    class Meta:
        model=Staff
        fields ='__all__'

class ToyForm(forms.ModelForm):
    class Meta:
        model=Toy
        fields ='__all__'        
