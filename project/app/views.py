from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Dept,Emp,Query
import random
from django.conf import settings 
from django.contrib import messages


# Create your views here.
def landing(req):
    return render(req, 'landing.html')

def login(req):
    if req.method == 'POST':
        e = req.POST.get('email')
        p = req.POST.get('password')
        if e == 'admin@gmail.com' and p == 'admin':
            req.session['admin_e'] = e
            req.session['admin_p'] = p
            req.session['admin_n'] = 'admin'
            return redirect('dashboard')
        else:
            user=Emp.objects.filter(emp_email=e)
            if user:
               user=Emp.objects.get(emp_email=e)
               if e==user.emp_email and p==user.emp_password:
                   req.session['emp_id']=user.id
                   req.session['emp_name']=user.emp_name
                   return redirect('emppanel')
               else:
                    x={'g':"wrong password or username"}
                    return render(req,'login.html',{'data':x})
            else:
                x={'g':"Invalid Email"}
                return render(req,'login.html',{'data':x})
    return render(req, 'login.html')



def password_reset(req):
    return render(req,'forget_password.html')

def reset_pass_code(req):
    if req.method == 'POST':
        email = req.POST.get('email')
        otp = random.randint(1000, 9999)

        send_mail(
            subject="Mail From Facebook",
            message=f"Hi,\n\nYour email: {email}\nYour OTP for reset password is: {otp}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],             
            fail_silently=False,
        )
        req.session['reset_otp'] = otp
        req.session['reset_email'] = email
        return render(req, 'set_new_password.html')
    return render(req, 'forget_password.html')
        
def confirm_password(req):
    if 'reset_otp' in req.session and 'reset_email' in req.session:
        if req.method=="POST":
            new_password=req.POST.get('password')
            confirm_password=req.POST.get('confirm_password')
            if new_password==confirm_password:
                return redirect('login')
            else:
                return redirect('set_new_password')
        
            

def logout(req):

    # Admin logout
    if 'admin_e' in req.session:
        req.session.flush()
        return redirect("landing")

    # Employee logout
    elif 'emp_id' in req.session:
        req.session.flush()
        return redirect("login")

    # If no session
    else:
        return redirect("login")

def dashboard(req):
    if 'admin_e' in req.session and 'admin_p' in req.session:

        a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }

        deptdata = Dept.objects.all()   

        total_users = Emp.objects.count()
        total_employees = Emp.objects.count()
        total_departments = Dept.objects.count()
        total_queries = Query.objects.count()

        return render(req, 'dashboard.html', {
            'data': a_data,
            'deptdata': deptdata,
            'total_users': total_users,
            'total_employees': total_employees,
            'total_departments': total_departments,
            'total_queries': total_queries,
        })

    return redirect('login')

# ---------------BUTTONS-----------------------------
def add_employees(req):
    if 'admin_e' in req.session and 'admin_p' in req.session:
        a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
        deptdata = Dept.objects.all()
        return render(req, 'dashboard.html', {'data': a_data, 'deptdata': deptdata})
    return render(req, 'login.html', {'msg': {'msg': 'login First'}})

def show_employee(req):
    if 'admin_e' not in req.session or 'admin_p' not in req.session:
        return redirect('login')

    a_data = {
        'email': req.session['admin_e'],
        'password': req.session['admin_p'],
        'name': req.session['admin_n']
    }

    all_emp = Emp.objects.all()
    deptdata = Dept.objects.all()

    # ===== GET SEARCH VALUES =====
    name = req.GET.get('name')
    email = req.GET.get('email')
    contact = req.GET.get('contact')
    dept = req.GET.get('dept')

    # ===== APPLY FILTERS =====
    if name:
        all_emp = all_emp.filter(emp_name__icontains=name)

    if email:
        all_emp = all_emp.filter(emp_email__icontains=email)

    if contact:
        all_emp = all_emp.filter(emp_contact__icontains=contact)

    if dept:
        all_emp = all_emp.filter(emp_department__dept_name__icontains=dept)

    return render(req, 'dashboard.html', {
        'data': a_data,
        'all_emp': all_emp,
        'deptdata': deptdata
    })



def add_department(req):
    if 'admin_e' in req.session and 'admin_p' in req.session:
        a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
        deptdata = Dept.objects.all()
        return render(req, 'dashboard.html', {'data': a_data, 'deptdata': deptdata})
    return render(req, 'login.html', {'msg': {'msg': 'login First'}})

# def show_department(req):
#     if 'admin_e' in req.session and 'admin_p' in req.session:
#         a_data = {
#             'email': req.session['admin_e'],
#             'password': req.session['admin_p'],
#             'name': req.session['admin_n']
#         }
#         deptdata = Dept.objects.all()
#         return render(req, 'dashboard.html', {'data': a_data, 'deptdata': deptdata})
#     return render(req, 'login.html', {'msg': {'msg': 'login First'}})



# -------------------------FORMS----------------------------------------------
def save_department(req):
    if req.method=="POST":
        dname = req.POST.get('dept_name')
        description = req.POST.get('description')
        deptdata=Dept.objects.filter(dept_name=dname)
        if not deptdata:
            Dept.objects.create(dept_name=dname,description=description)
            return redirect('add_department')
        else:
            return redirect('add_department')
    return redirect('login')



def addemp(req):
    if 'admin_e' in req.session and 'admin_p' in req.session:
        a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }

        deptdata = Dept.objects.all()   # ✅ always send

        if req.method == "POST":
            emp_name = req.POST.get('emp_name')
            emp_email = req.POST.get('emp_email')
            emp_contact = req.POST.get('emp_contact')
            emp_password = req.POST.get('emp_password')

            dept_id = req.POST.get("emp_department")  # ✅ from dropdown

            # ✅ if no department exists
            if not deptdata.exists():
                messages.error(req, "Please add Department First")
                return render(req, 'dashboard.html', {
                    'data': a_data,
                    "add_employees": True,
                    'deptdata': deptdata
                })

            # ✅ if employee already exists
            if Emp.objects.filter(emp_email=emp_email).exists():
                messages.error(req, "This Employee Already Exist")
                return render(req, 'dashboard.html', {
                    'data': a_data,
                    "add_employees": True,
                    'deptdata': deptdata
                })

            # ✅ validate department selection
            if not dept_id:
                messages.error(req, "Please select a department")
                return render(req, 'dashboard.html', {
                    'data': a_data,
                    "add_employees": True,
                    'deptdata': deptdata
                })

            dept_obj = Dept.objects.get(id=dept_id)

            # ✅ create employee with department
            Emp.objects.create(
                emp_name=emp_name,
                emp_email=emp_email,
                emp_contact=emp_contact,
                emp_password=emp_password,
                emp_department=dept_obj   
            )

            messages.success(req, "Employee Added Successfully!")

            send_mail(
                "Mail From Facebook",
                f'Hii {emp_name}, your Contact: {emp_contact} and your password is: {emp_password}',
                "sy21022004@gmail.com",
                [emp_email],
                fail_silently=False,
            )

            return render(req, 'dashboard.html', {
                'data': a_data,
                "add_employees": True,
                'deptdata': deptdata
            })

        return render(req, 'dashboard.html', {
            'data': a_data,
            "add_employees": True,
            'deptdata': deptdata
        })

    else:
        return redirect('login')

        

# ----------------------------------------------------------------------------------------
def emppanel(req):
    if 'emp_id' not in req.session:
        return redirect("login")

    emp_id = req.session.get("emp_id")
    emp_data = Emp.objects.get(id=emp_id)

    data = {
        'emp_name': emp_data.emp_name,
        'emp_email': emp_data.emp_email,
        'emp_contact': emp_data.emp_contact,
        'emp_password': emp_data.emp_password,
        'emp_department': emp_data.emp_department
    }

    all_queries = Query.objects.filter(Email=emp_data.emp_email).order_by("-id")

    pending_list = all_queries.filter(status="Pending")
    done_list = all_queries.filter(status="Done")

    total_queries = all_queries.count()
    pending_queries = pending_list.count()
    done_queries = done_list.count()

    return render(req, "emppanel.html", {
        "data": data,
        "all_queries": all_queries,
        "pending_list": pending_list,
        "done_list": done_list,
        "total_queries": total_queries,
        "pending_queries": pending_queries,
        "done_queries": done_queries,
    })

# -------------------QUERIS-------------------------------------------

def all_queries(req):

    if 'admin_e' in req.session and 'admin_p' in req.session:
        a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }

        qdata = Query.objects.all()

        
        reply_query = None
        rid = req.GET.get("reply_id")

        if rid:
            reply_query = Query.objects.get(id=rid)

        return render(req, 'dashboard.html', {
            'data': a_data,
            'qdata': qdata,
            'reply_query': reply_query
        })

    else:
        msg = {'msg': 'login first'}
        return render(req, "login.html", {'msg': msg})


def add_query(req):
    if req.method == "POST":
        emp_name = req.POST.get('name')
        emp_email = req.POST.get('email')
        emp_department = req.POST.get('department')
        emp_query = req.POST.get('query')

        Query.objects.create(
            Name=emp_name,
            Email=emp_email,
            department=emp_department,
            Query=emp_query,
            status="Pending"
        )

        messages.success(req, "Query Submitted Successfully!")
        return redirect("/emppanel/?page=add_query")   

    return redirect("/emppanel/?page=add_query")
    

def reply_save(req):
    if req.method == "POST":
        qid = req.POST.get("qid")
        admin_rep = req.POST.get("admin_rep")

        q = Query.objects.get(id=qid)
        q.admin_rep = admin_rep
        q.status = "Done"
        q.save()

        return redirect("/all_queries/?page=all_queries")

    return redirect("/all_queries/?page=all_queries")


def search_employees(req):
    if 'admin_e' not in req.session:
        return redirect("login")

    all_emp = Emp.objects.all().order_by("-id")

    # GET filters
    name = req.GET.get("name")
    email = req.GET.get("email")
    contact = req.GET.get("contact")
    dept = req.GET.get("dept")

    if name:
        all_emp = all_emp.filter(emp_name__icontains=name)

    if email:
        all_emp = all_emp.filter(emp_email__icontains=email)

    if contact:
        all_emp = all_emp.filter(emp_contact__icontains=contact)

    if dept:
        all_emp = all_emp.filter(emp_department__icontains=dept)

    return render(req, "show_employees.html", {
        "all_emp": all_emp
    })
















































