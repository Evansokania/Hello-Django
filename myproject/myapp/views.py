from django.shortcuts import render
from .models import Employee


# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, "myapp/index.html", {"employees": employees})
