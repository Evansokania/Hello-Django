"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import register, user_login, employee_list, add_employee, edit_employee, delete_employee,logout_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', employee_list, name='home'),
    path("register/", register, name="register"),
    # path("login/", user_login, name="login"),
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    #path("logout/", user_logout, name="logout"),
    path("employees/", employee_list, name="employee-list"),
    path("add/", add_employee, name="add-employee"),
    path("edit/<int:pk>/", edit_employee, name="edit-employee"),
    path("delete/<int:pk>/", delete_employee, name="delete-employee"),
]


