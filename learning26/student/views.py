from django.shortcuts import render,redirect
from .models import Service
from .forms import ServiceForm

# Create your views here.

def studentdetails(request):
    stud={"name":"xyz","age": 20, "city":"surat"}
    return render(request,"student/studentdetails.html",stud)
def studentmarks(request):
    stud1={"name":"abc","marks":78, "city":"ahmedabad"}
    return render(request,"student/studentmarks.html",stud1)
def studentfees(request):
    stud2={"name":"gdk","fees":24000}
    return render(request,"student/studentfees.html",stud2)

def servicelist(request):
    Service= Service.Object.all()
    return render(request,"student/serviceList.html",{"services":services})

def createService(request):

    if request.method =="POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("serviceList")
        else:
            return render(request,"student/createService.html",{"form":form})    
    else:
        form = ServiceForm()
        return render(request,"student/createService.html",{"form":form})

