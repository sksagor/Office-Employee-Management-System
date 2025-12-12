from django.shortcuts import render, HttpResponse
from .models import Employee,Department,Role
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    print (context)
    return render(request,'all_emp.html',context)

def add_emp(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        # Convert to int, ensure keys match form names
        salary = int(request.POST['salary'])
        dept_id = request.POST['dept'] 
        role_id = request.POST['role']
        phone = int(request.POST['phone'])
        
        # Use dept_id and role_id from the form data (which is correct)
        new_emp = Employee(
            first_name=first_name,
            last_name=last_name,
            salary=salary,
            phone=phone,
            dept_id=dept_id,
            role_id=role_id,
            hire_date=datetime.now()
        )
        new_emp.save()
        return HttpResponse('Employee added successfully')
        
    elif request.method == 'GET':
        # Send Department and Role objects to the template for dropdowns
        depts = Department.objects.all()
        roles = Role.objects.all()
        context = {
            'all_depts': depts,
            'all_roles': roles
        }
        return render(request,'add_emp.html', context)
        
    else:
        return HttpResponse("Error: Employee had not added!")

def view_emp(request):
    return render(request,'view_emp.html')

def remove_emp(request, emp_id= 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully.")
        except:
            return HttpResponse("Please Enter a valid EMP ID")
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }

    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        dept = request.POST.get('dept', '')
        role = request.POST.get('role', '')
        
        emps = Employee.objects.all()
        
        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name=dept)
        if role:
            emps = emps.filter(role__name=role)
        
        context = {
            'emps': emps,
            'name': name,
            'selected_dept': dept,
            'selected_role': role
        }
        return render(request, 'all_emp.html', context)
    
    elif request.method == 'GET': 
        # You need to pass all_depts and all_roles for the GET request
        context = {
            'all_depts': Department.objects.all(),
            'all_roles': Role.objects.all()
        }
        return render(request, 'filter_emp.html', context)
    
    else:  
        return HttpResponse('An exception Occurred.')
