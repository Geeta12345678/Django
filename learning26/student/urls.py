from django.urls import path
from.import views

urlpatterns= [
    path("student/",views.studentdetails),
    path("marks/",views.studentmarks),
    path("fees/",views.studentfees)
]