from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
   # path('trial/', views.trial, name = 'trial'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('searchattendence/', views.searchAttendence, name='searchattendence'),
    path('account/', views.facultyProfile, name='account'),

    path('updateStudentRedirect/', views.updateStudentRedirect, name='updateStudentRedirect'),
    path('updateStudent/', views.updateStudent, name='updateStudent'),
    path('attendence/', views.takeAttendence, name='attendence'),
    path('', views.home, name='home'),
    path('studentprofile/', views.studentprofile, name='studentprofile'),
    path('teacherprofile/', views.teacherprofile, name='teacherprofile'),
    path('studentlogin/', views.studentlogin, name='studentlogin'),
    path('studentlogout/', views.studentlogout, name='studentlogout'),

    path('SearchAttendence/', views.SearchAttendence, name='SearchAttendence'),
    path('TakeAttendence/', views.TakeAttendence, name='TakeAttendence'),
    path('UpdateStudent/', views.UpdateStudent, name='UpdateStudent'),
    path('AddStudent/', views.AddStudent, name='AddStudent'),
    path('MyAttendence/', views.MyAttendence, name='MyAttendence'),
    path('AttendenceReports/', views.AttendenceReports, name='AttendenceReports'),
    path('Defaulters/', views.Defaulters, name='Defaulters'),
    
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='Attendence_Sys/password_reset.html'),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='Attendence_Sys/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='Attendence_Sys/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='Attendence_Sys/password_reset_complete.html'), name='password_reset_complete'),

    
    
    

    


    # path('video_feed/', views.videoFeed, name='video_feed'),
    # path('videoFeed/', views.getVideo, name='videoFeed'),
]