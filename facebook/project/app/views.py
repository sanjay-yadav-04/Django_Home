from django.shortcuts import render,redirect
from .models import Department
# Create your views here.
def landing(req):
    return render(req,'landing.html')

def login(req):
    if req.method== 'POST':
        email=req.POST.get('email')
        password=req.POST.get('password')
        if email== 'admin@gmail.com' and password == 'admin':
            req.session['admin_email']=email
            req.session['admin_password']=password
            req.session['admin_name']='admin'
            return redirect('admin_panel')
    return render(req,'login.html')

def admin_panel(req):
    if 'admin_email' in req.session and 'admin_password' in req.session:
        admin_data={
            'email':req.session['admin_email'],
            'password':req.session['admin_password'],
            'name':req.session['admin_name']
        }
        department_data=Department.objects.all()
        return render(req,'admin_panel.html',{'data':admin_data,'department_data':department_data})

def add_department(req):
    if req.method == 'POST':
        department_name=req.POST.get('dept_name')
        department_Description=req.POST.get('dept_Description')
        department_data=Department.objects.filter(dept_name=department_name)
        if not department_data:
            Department.objects.create(dept_name=department_name,dept_Description=department_Description)
            return redirect('admin_panel')
    return redirect('login')

def show_department(req):
    if 'admin_email' in req.session and 'admin_password' in req.session:
        admin_data={
            'email':req.session['admin_email'],
            'password':req.session['admin_password'],
            'name':req.session['admin_name']
        }
        department_data=Department.objects.all()
        return render(req,'admin_panel.html',{'admin_data':admin_data,'department_data':department_data})
    return render(req,'login.html',{'msg':'Login First'})
    
    








def logout(req):
    pass
def empdata(req):
    pass
def querydata(req):
    pass
def deptdata(req):
    pass
def donequerydata(req):
    pass
def dept_count(req):
    pass
def emp_count(req):
    pass
def query_count(req):
    pass








