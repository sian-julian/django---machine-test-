from django.shortcuts import render,redirect
from .forms import Employeeform
from .models import *

# Create your views here.

def add_emp(request):
    if request.method == 'POST':
        form=Employeeform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_list.html')
    else:
        form=Employeeform()
    return render(request,'add_employee.html',{'form':form})


def employee_list(request):
    emp =Employee.objects.all()
    return render(request,'employee_list.html',{'emp': emp})

def update_emp(request,id):
    emp=Employee.objects.get(id=id)
    if request.method == 'POST':
        form=Employeeform(request.POST,request.FILES,instance=emp)
        if form.is_valid():
            form.save()
            return redirect('employee_list.html')
    else:
        form=Employeeform(instance=emp)
    return render(request,'update_employee.html',{'form':form})


