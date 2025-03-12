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
from App.views import more_info,college_magazine,newsletter,seminars,workshops,cultural_events,sports_activities,placement_opportunities,graduation_view,scholarships,campus_life,library_view,edit_username,edit_password,edit_student,update_student,homepage,home,about,courses,enroll,Committee,Alumni,news_events,admissions,fill_application,submit_application,submit_documents,entrance_exam,start_exam,exam_submission,interview,next_step,admission_offer,fee_payment,contact,More,student_register,teacher_register,student_home_page,teacher_home_page,admin_home_page,login_all,view_student_by_admin,approve_student,delete_student,view_teacher_by_admin,log_out
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
    path('submit_application/',submit_application, name='submit_application'),  # New URL
    path('submit_documents/',submit_documents, name='submit_documents'),
    path('entrance_exam/',entrance_exam, name='entrance_exam'),
    path('start_exam/', start_exam, name='start_exam'),
    path('exam_submission/', exam_submission, name='exam_submission'),
    path('interview',interview,name='interview'),
     path('next_step/', next_step, name='next_step'),
    path('admission_offer',admission_offer,name='admission_offer'),
    path('fee_payment',fee_payment,name='fee_payment'),
    
    
    path('contact',contact,name='contact'),
    path('more',More,name='more'),
    path('more_info/',more_info, name='more_info'),
    path('college_magazine/',college_magazine, name='college_magazine'),
    path('newsletter/', newsletter, name='newsletter'),
    path('seminars/', seminars, name='seminars'),
    path('workshops/', workshops, name='workshops'),
    path('cultural_events/', cultural_events, name='cultural_events'),
    path('sports_activities/', sports_activities, name='sports_activities'),
    path('placement_opportunities/', placement_opportunities, name='placement_opportunities'),
    path("student",student_register,name='student_register'),
    path("teacher",teacher_register,name='teacher_register'),
    path("login/",login_all,name='login_all'),
    path("studenthome",student_home_page),
    path("home/", student_home_page, name="student_home_page"),
    path("edit_username/", edit_username, name="edit_username"),
    path("edit-password/", edit_password, name="edit_password"),
    path("edit_student/", edit_student, name="edit_student"),  # Ensure the URL ends with a "/"
    path('update_student/<int:id>/', update_student, name='update_student'),
    path("studenthome1/",student_home_page,name='studenthome1'),
    path("teacherhome",teacher_home_page),
    path("teacherhome1",teacher_home_page),
    path("adminhome",admin_home_page),
    path("viewstudentadmin/", view_student_by_admin, name="viewstudentadmin"),  # Correct name
    path("approve_student/<int:id>/", approve_student, name="approve_student"),  
    path("delete_student/<int:id>/", delete_student, name="delete_student"),
    path("viewteacheradmin",view_teacher_by_admin),
    path('graduation/', graduation_view, name='graduation'),
    path('scholarships/', scholarships, name='scholarships'),
    path("campuslife/", campus_life, name="campus_life"),  # URL for Campus Life page
    path('library/', library_view, name='library_page'),
    path("logout/",log_out),
]
