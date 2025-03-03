"""
URL configuration for PR1 project.

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
from App.views import edit_username,edit_password,edit_student,update_student,homepage,home,about,courses,enroll,Committee,Alumni,news_events,admissions,fill_application,submit_documents,entrance_exam,interview,admission_offer,fee_payment,contact,student_register,teacher_register,student_home_page,teacher_home_page,admin_home_page,login_all,view_student_by_admin,approve_student,delete_student,view_teacher_by_admin,log_out
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name='homepage'),
    path('home',home, name='home'),
    path('about',about,name='about'),
    path('courses',courses,name='courses'),
    path('enroll/<str:course_name>/', enroll, name='enroll'),
    path('committee',Committee,name='committee'),
    path('Alumni',Alumni,name='Alumni'),
    path('news_events',news_events,name='news_events'),
    path('admissions',admissions,name='admissions'),
    path('fill_application/',fill_application, name='fill_application'),
    path('submit_documents/',submit_documents, name='submit_documents'),
    path('entrance_exam/',entrance_exam, name='entrance_exam'),
    path('interview',interview,name='interview'),
    path('admission_offer',admission_offer,name='admission_offer'),
    path('fee_payment',fee_payment,name='fee_payment'),
    
    
    path('contact',contact,name='contact'),
    path("student",student_register,name='student_register'),
    path("teacher",teacher_register,name='teacher_register'),
    path("login/",login_all,name='login_all'),
    path("studenthome",student_home_page),
    path("home/", student_home_page, name="student_home_page"),
    path("edit_username/", edit_username, name="edit_username"),
    path("edit-password/", edit_password, name="edit_password"),
    path('edit_student',edit_student,name='edit_student'),
    path('update_student/<int:id>/', update_student, name='update_student'),
    path("studenthome1/",student_home_page,name='studenthome1'),
    path("teacherhome",teacher_home_page),
    path("teacherhome1",teacher_home_page),
    path("adminhome",admin_home_page),
    path("viewstudentadmin",view_student_by_admin),
    path("approve_student/<int:id>/", approve_student, name="approve_student"),
    path("del/<int:id>/", delete_student, name="delete_student"),
    path("viewteacheradmin",view_teacher_by_admin),
    path("logout/",log_out),
]
