from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, EmployeeForm
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


@login_required
def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("employee-list")
    else:
        form = EmployeeForm(instance=employee)
    return render(request, "myapp/edit_employee.html", {"form": form, "employee": employee})

@login_required
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        employee.delete()
        return redirect("employee-list")
    return render(request, "myapp/delete_employee.html", {"employee": employee})