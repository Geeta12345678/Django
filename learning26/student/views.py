from django.shortcuts import render

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
