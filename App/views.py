from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages  # Import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from . models import User,Student,Teacher
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.



def homepage(request):
    return render(request,'basehomepage.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'aboutus.html')

def courses(request):
    return render(request, 'courses.html')
def enroll(request, course_name):
    return render(request, 'enroll.html', {'course_name': course_name})

def Committee(request):
    return render(request, 'Committee.html')

def Alumni(request):
    return render(request, 'Alumni.html')

def news_events(request):
    return render(request, 'news_events.html')


def admissions(request):
    return render(request, 'admissions.html')
def fill_application(request):
    return render(request, 'fill_application.html')

def submit_documents(request):
    return render(request, 'submit_documents.html')

def entrance_exam(request):
    return render(request, 'entrance_exam.html')

def interview(request):
    return render(request, 'interview.html')

def admission_offer(request):
    return render(request, 'admission_offer.html')

def fee_payment(request):
    return render(request, 'fee_payment.html')

def contact(request):
    return render(request, 'contact.html')


def student_register(request):
    if request.method=="POST":
        fn=request.POST['firstname']
        ln=request.POST['lastname']
        em=request.POST['email']
        un=request.POST['username']
        p=request.POST['password']
        ad=request.POST['address']
        phn=request.POST['phonenumber']
        x=User.objects.create_user(first_name=fn,last_name=ln,email=em,username=un,password=p,usertype="student",is_active=False)
        x.save()
        y=Student.objects.create(student_id=x,address=ad,phone_number=phn)
        y.save()
        return redirect('login_all')
    #     return HttpResponse("student registration successfulll")
    # else:
    return render(request,"stud_reg.html")
    
 
 
def teacher_register(request):
    if request.method == "POST":
        fn = request.POST["firstname"]
        ln = request.POST["lastname"]
        e = request.POST["email"]
        u = request.POST["username"]
        p = request.POST["password"]
        a = request.POST["address"]
        phn = request.POST["phonenumber"]
        ex = request.POST["experience"]
        sa = request.POST["salary"]

        # Create user and teacher objects
        x = User.objects.create_user(
            first_name=fn,
            last_name=ln,
            username=u,
            password=p,
            email=e,
            is_active=True,
            is_staff=True
        )
        x.save()

        y = Teacher.objects.create(
            teacher_id=x,
            address=a,
            phone_number=phn,
            experience=ex,
            salary=sa
        )
        y.save()

        return redirect('login_all')  # Ensure 'login_all' matches your URL name in urls.py

    return render(request, "teach_reg.html")  # Ensure 'teach_reg.html' exists in the templates folder


def admin_home_page(request):
    return render(request,"admin_home_page.html")

def student_home_page(request):
    if not request.user.is_authenticated:
        return redirect('login_all')

    try:
        x = Student.objects.get(student_id=request.user)
    except Student.DoesNotExist:
        messages.error(request, "No student record found for your account.")
        return redirect('home')  # Redirect to a relevant page

    context = {
        'firstname': x.student_id.first_name,
        'lastname': x.student_id.last_name,
    }
    return render(request, "student_home_page.html", context)

@login_required
def edit_username(request):
    if request.method == "POST":
        new_username = request.POST["username"]
        
        # Check if the username already exists
        if User.objects.filter(username=new_username).exists():
            messages.error(request, "Username already taken. Try another one.")
            return redirect("edit_username")

        # Update the username
        request.user.username = new_username
        request.user.save()
        messages.success(request, "Username updated successfully.")
        return redirect("student_home_page")

    return render(request, "edit_username.html")


@login_required
def edit_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keep user logged in after password change
            messages.success(request, "Password updated successfully.")
            return redirect("student_home_page")
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = PasswordChangeForm(request.user)

    return render(request, "edit_password.html", {"form": form})


















def teacher_home_page(request):
    if not request.user.is_authenticated:
        return redirect('login_all')  

    x = get_object_or_404(Teacher, teacher_id=request.user)
    
    context = {
        'firstname': x.teacher_id.first_name,
        'lastname': x.teacher_id.last_name,
    }
    return render(request, "teacher_home_page.html", context)
   
def login_all(request):
    if request.method == "POST":
        us = request.POST.get("username")
        pas = request.POST.get("password")

        user = authenticate(request, username=us, password=pas)

        if user is not None:
            login(request, user)  # Authenticate and login user

            if user.is_superuser:
                return redirect('admin_home_page')  # Admin Home Page

            elif user.is_staff:
                request.session['teacher_id'] = user.id
                return redirect('teacher_home_page')  # Teacher Home Page

            else:  # Student Login
                request.session["student_id"] = user.id
                return redirect('studenthome1')  # Redirecting to student home page
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login_all')  # Reload Login Page on Error

    return render(request, "login_all.html")  # Render login page
# def login_all(request):
#     if request.method=="POST":
#       us=request.POST["username"]
#       pas=request.POST["password"]
#       user=authenticate(request,username=us,password=pas)
#       if user is not None and user.is_superuser==1:
#         return redirect(admin_home_page)
#       elif user is not None and user.is_staff==1:
#         login(request,user)
#         request.session['teacher_id']=user.id
#         return redirect(teacher_home_page)
#       elif user is not None and  user.is_active==1:
#         login(request,user)
#         request.session["student_id"]=user.id
#         return redirect(student_home_page)
        
#     else:
#         return render(request,"login_all.html")
    
    
def view_student_by_admin(request):
    s=Student.objects.select_related('student_id').all()
    return render (request,"view_student.html",{'func':s})   

def approve_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.is_approved = True  # Assuming `is_approved` field exists
    student.save()
    return redirect('view_student_by_admin')  # Redirect to student list page

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('view_student_by_admin')  # Redirect after deletion

    
def view_teacher_by_admin(request):
   v=Teacher.objects.select_related('teacher_id').all()
   return render (request,'view_teacher.html',{'fun':v})


# def edit_student(request):
#    x=request.session.get('student_id')
#    y=Student.objects.get(student_id_id=x)
#    z=User.objects.get(id=x)
#    return render (request,"edit_student.html",{'views':y,'data':z})

def edit_student(request):
    x = request.session.get('student_id')
    
    if not x:
        messages.error(request, "Session expired. Please log in again.")
        return redirect('login_all')

    y = get_object_or_404(Student, student_id_id=x)
    z = get_object_or_404(User, id=x)
    
    return render(request, "edit_student.html", {'views': y, 'data': z})

def update_student(request, id):
    if request.method == 'POST':
        q = get_object_or_404(User, id=id)
        p = get_object_or_404(Student, student_id_id=id)

        q.first_name = request.POST["firstname"]
        q.last_name = request.POST["lastname"]
        q.email = request.POST["email"]
        q.username = request.POST["username"]
        q.set_password(request.POST["password"])  # Secure password handling

        p.address = request.POST["address"]
        p.phone_number = request.POST["phonenumber"]

        q.save()
        p.save()

        messages.success(request, "Profile updated successfully! Please log in again.")
        return redirect('login_all')  # Logout required after password change

    return redirect('edit_student')






# def update_student(request,id):
#    if request.method=='POST':
#       q=User.objects.get(id=id)
#       p=Student.objects.get(student_id_id=q)

#       q.first_name=request.POST["firstname"]
#       q.last_name=request.POST["lastname"]
#       q.email=request.POST["email"]
#       q.username=request.POST["username"]
#       q.password=request.POST["password"]
#       print(q)
#       q.save()
#       p.address=request.POST["address"]
#       p.phone_number=request.POST["phonenumber"]
#       print(p)
#       p.save()
#       return redirect(student_home_page)


def log_out(request):
   logout(request)
   return render(request, 'log_out.html')