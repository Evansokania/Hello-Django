from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from .models import Employee

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")

# def employee_list(request):
#     employees = Employee.objects.all()
#     return render(request, "myapp/employee_list.html", {"employees": employees})


def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employee-list")
    else:
        form = EmployeeForm()

    return render(request, "myapp/add_employee.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("employee-list")
    else:
        form = RegisterForm()
    return render(request, "myapp/register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("employee-list")
    else:
        form = AuthenticationForm()
    return render(request, "myapp/login.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect("login")

@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, "myapp/employee_list.html", {"employees": employees})
