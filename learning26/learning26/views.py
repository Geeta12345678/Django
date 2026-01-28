from django.http import HttpResponse
from django.shortcuts import render

def test(request):
       return HttpResponse("hello")

def aboutus(request):
     return render(request,"aboutus.html")

def contactus(request):
     return render(request,"contactus.html")

def home(request):
     return render(request,"home.html")

def movies(request):
     return render(request,"movies.html")

def shows(request):
     return render(request,"shows.html")

def news(request):
     return render(request,"news.html")

def recipe(request):
     ingredient ={"maggie","tomato"}
     data= {"name":"meggie","time": 2,"ingredient":ingredient}
     return render(request,"recipe.html",data)


