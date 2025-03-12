from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages  
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

def submit_application(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        course = request.POST.get('course')
        address = request.POST.get('address')

        context = {
            "name": name,
            "email": email,
            "phone": phone,
            "dob": dob,
            "course": course,
            "address": address
        }
        return render(request, 'application_received.html', context)
    else:
        return render(request, 'error.html', {"message": "Invalid Request"})
def submit_documents(request):
    return render(request, 'submit_documents.html')

def entrance_exam(request):
    return render(request, 'entrance_exam.html')
def start_exam(request):
    return render(request, 'start_exam.html')
def exam_submission(request):
    if request.method == "POST":
        score = 0
        answers = {
            "q1": "12",
            "q2": "Delhi",
        }

        for question, correct_answer in answers.items():
            if request.POST.get(question) == correct_answer:
                score += 1

        return render(request, 'exam_result.html', {"score": score})

    return render(request, 'start_exam.html')


def interview(request):
    return render(request, 'interview.html')
def next_step(request):
    return render(request, 'next_step.html')

def admission_offer(request):
    return render(request, 'admission_offer.html')

def fee_payment(request):
    return render(request, 'fee_payment.html')

def contact(request):
    return render(request, 'contact.html')

def More(request):
    return render(request, 'more.html')

def more_info(request):
    return render(request, 'more_info.html')

def college_magazine(request):
    return render(request, 'college_magazine.html')

def newsletter(request):
    return render(request, 'newsletter.html')

def seminars(request):
    return render(request, 'seminars.html')

def workshops(request):
    return render(request, 'workshops.html')

def cultural_events(request):
    return render(request, 'cultural_events.html')

def sports_activities(request):
    return render(request, 'sports_activities.html')

def placement_opportunities(request):
    return render(request, 'placement_opportunities.html')


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

        return redirect('login_all')  

    return render(request, "teach_reg.html")  


def admin_home_page(request):
    return render(request,"admin_home_page.html")

def student_home_page(request):
    if not request.user.is_authenticated:
        return redirect('login_all')

    try:
        x = Student.objects.get(student_id=request.user)
    except Student.DoesNotExist:
        messages.error(request, "No student record found for your account.")
        return redirect('studenthome1')  # Redirect to a relevant page

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
    if request.method=="POST":
      us=request.POST["username"]
      pas=request.POST["password"]
      user=authenticate(request,username=us,password=pas)
      if user is not None and user.is_superuser==1:
        return redirect(admin_home_page)
      elif user is not None and user.is_staff==1:
        login(request,user)
        request.session['teacher_id']=user.id
        return redirect(teacher_home_page)
      elif user is not None and  user.is_active==1:
        login(request,user)
        request.session["student_id"]=user.id
        return redirect(student_home_page)
        
    else:
        return render(request,"login_all.html")
    
    
def view_student_by_admin(request):
    students = Student.objects.select_related('student_id').all()
    return render(request, "view_student.html", {'func': students})   

def approve_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.is_approved = True  # Assuming `is_approved` exists
    student.save()

    # ✅ Corrected redirection
    return redirect('viewstudentadmin')  # Match `name="viewstudentadmin"` in urls.py

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return render(request, 'delete_success.html', {'message': 'Student deleted successfully!'})

def view_teacher_by_admin(request):
   v=Teacher.objects.select_related('teacher_id').all()
   return render (request,'view_teacher.html',{'fun':v})


def edit_student(request):
    student_id = request.session.get('student_id', None)  # Get session ID (default to None)

    if student_id:  
        student = get_object_or_404(Student, student_id_id=student_id)
        user = get_object_or_404(User, id=student_id)
    else:
        student = None  # If session ID is missing, student/user will be None
        user = None

    if request.method == 'POST':
        if user and student:
            user.first_name = request.POST['firstname']
            user.last_name = request.POST['lastname']
            user.email = request.POST['email']
            user.username = request.POST['username']
            user.set_password(request.POST['password'])  # Encrypt password
            user.save()

            student.phone_number = request.POST['phonenumber']
            student.address = request.POST['address']
            student.save()

            return redirect('student_home_page')  # Redirect to student home

    return render(request, "edit_student.html", {'student': student, 'user': user})

def update_student(request,id):
   if request.method=='POST':
      q=User.objects.get(id=id)
      p=Student.objects.get(student_id_id=q)

      q.first_name=request.POST["firstname"]
      q.last_name=request.POST["lastname"]
      q.email=request.POST["email"]
      q.username=request.POST["username"]
      q.password=request.POST["password"]
      print(q)
      q.save()
      p.address=request.POST["address"]
      p.phone_number=request.POST["phonenumber"]
      print(p)
      p.save()
      return redirect(student_home_page)



def graduation_view(request):
    return render(request, 'graduation.html')

def scholarships(request):
    return render(request, 'scholarships.html')

def campus_life(request):
    return render(request, "campus_life.html")  # Ensure the template name matches

def library_view(request):
    return render(request, 'library.html')

def log_out(request):
   logout(request)
   return render(request, 'log_out.html')