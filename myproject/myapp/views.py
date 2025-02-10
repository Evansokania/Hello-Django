from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, "myapp/index.html", {"employees": employees})


def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employee-list")
    else:
        form = EmployeeForm()

    return render(request, "myapp/add_employee.html", {"form": form})
