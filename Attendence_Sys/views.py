from django.shortcuts import render, redirect
from django.http import HttpResponse, StreamingHttpResponse

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import Student, Attendence
from .filters import AttendenceFilter,StudentFilter,ReportFilter

# from django.views.decorators import gzip

from .recognizer import Recognizer
from datetime import date




def home(request):
    return render(request,'Attendence_Sys/home.html')



@login_required(login_url = 'studentlogin')
def AddStudent(request):
    try:
        student = request.user.faculty
        return redirect(teacherprofile)

    except:
        student=request.user
    studentForm = CreateStudentForm()

    if request.method == 'POST':
        details = {
            'branch':request.POST['branch'],
            'year': request.POST['year'],
            'section':request.POST['section'],}
        ID = request.POST['registration_id']
        studentForm = CreateStudentForm(data = request.POST, files=request.FILES)
        # print(request.POST)
        stat = False 
        try:
            student = Student.objects.get(registration_id = request.POST['registration_id'])
            stat = True
        except:
            stat = False
        if studentForm.is_valid() and (stat == False):
            studentForm.save()
            reports=Reports(student_id=str(ID),
                           total=0,
                           count=0,
                           percentage=0,
                           section=details['section'],
                           branch=details['branch'],
                           year=details['year'])
            reports.save()
            name = studentForm.cleaned_data.get('firstname') +" " +studentForm.cleaned_data.get('lastname')
            messages.success(request, 'Student ' + name + ' was successfully added.')
            return redirect('AddStudent')
        else:
            messages.error(request, 'Student with Registration Id '+request.POST['registration_id']+' already exists.')
            return redirect('AddStudent')

    context = {'studentForm':studentForm}
    return render(request, 'Attendence_Sys/AddStudent.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('teacherprofile')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('teacherprofile')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'Attendence_Sys/login.html', context)

@login_required(login_url = 'teacherlogin')
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url = 'studentlogin')
def updateStudentRedirect(request):
    try:
        student = request.user.faculty
        return redirect(teacherprofile)

    except:
        student=request.user
    context = {}
    if request.method == 'POST':
        try:
            reg_id = request.user
            branch = request.POST['branch']
            student = Student.objects.get(registration_id = reg_id, branch = branch)
            updateStudentForm = CreateStudentForm(instance=student)
            context = {'form':updateStudentForm, 'prev_reg_id':reg_id, 'student':student}
        except:
            messages.error(request, 'Student Not Found')
            return redirect('UpdateStudent')
    return render(request, 'Attendence_Sys/student_update.html', context)

@login_required(login_url = 'studentlogin')
def updateStudent(request):
    try:
        student = request.user.faculty
        return redirect(teacherprofile)

    except:
        student=request.user
    if request.method == 'POST':
        
        context = {}
        try:
            student = Student.objects.get(registration_id = request.POST['prev_reg_id'])
            updateStudentForm = CreateStudentForm(data = request.POST, files=request.FILES, instance = student)
            if updateStudentForm.is_valid():
                updateStudentForm.save()
                messages.success(request, 'Updation Success')
                return redirect('UpdateStudent')
        except:
            messages.error(request, 'Updation Unsucessfull')
            return redirect('UpdateStudent')
    return render(request, 'Attendence_Sys/student_update.html', context)


@login_required(login_url = 'teacherlogin')
def takeAttendence(request):
    try:
        student = Student.objects.get(registration_id = request.user)
        return redirect(studentprofile)

    except:
        student=request.user
    if request.method == 'POST':
        details = {
            'branch':request.POST['branch'],
            'year': request.POST['year'],
            'section':request.POST['section'],
            'period':request.POST['period'],
            'faculty':request.user.faculty
            }
        if Attendence.objects.filter(date = str(date.today()),branch = details['branch'], year = details['year'], section = details['section'],period = details['period']).count() != 0 :
            messages.error(request, "Attendence already recorded.")
            return redirect('TakeAttendence')
        else:
            students = Student.objects.filter(branch = details['branch'], year = details['year'], section = details['section'])
            names = Recognizer(details)
            for student in students:
                if str(student.registration_id) in names:
                    stu= Reports.objects.get(student_id=str(student.registration_id))
                    x=stu.count
                    y=stu.total
                    x1=x+1
                    y1=y+1
                    stu.count=x1
                    stu.total=y1
                    z1=(x1/y1)*100

                    stu.percentage=z1
                    stu.save()
                    attendence = Attendence(Faculty_Name = request.user.faculty,
                    Student_ID = str(student.registration_id),
                    period = details['period'], 
                    branch = details['branch'], 
                    year = details['year'], 
                    section = details['section'],
                    status = 'Present')
                    attendence.save()
                    
                else:
                    stud= Reports.objects.get(student_id=str(student.registration_id))
                    x=stud.count
                    y=stud.total
                    y2=y+1
                    stud.count=x
                    stud.total=y2
                    if(x==0):
                        z2=0
                        
                    else:
                        z2=(x/y2)*100

                    stud.percentage=z2
                    stud.save()
                    attendence = Attendence(Faculty_Name = request.user.faculty,
                    Student_ID = str(student.registration_id),
                    period = details['period'],
                    branch = details['branch'], 
                    year = details['year'], 
                    section = details['section'])
                    attendence.save()
                    
            attendences = Attendence.objects.filter(date = str(date.today()),branch = details['branch'], year = details['year'], section = details['section'],period = details['period'])
            context = {"attendences":attendences, "ta":True}
            messages.success(request, "Attendence taking Success")
            return render(request, 'Attendence_Sys/attendence.html', context)        
    return render(request, 'Attendence_Sys/teacherprofile.html')



@login_required(login_url='teacherlogin')
def searchAttendence(request):
    try:
        student = Student.objects.get(registration_id = request.user)
        return redirect(studentprofile)

    except:
        student=request.user
    attendences = Attendence.objects.all()
    myFilter = AttendenceFilter(request.GET, queryset=attendences)
    attendences = myFilter.qs
    context = {'myFilter':myFilter, 'attendences': attendences, 'ta':False}
    return render(request, 'Attendence_Sys/attendence.html', context)



def MyAttendence(request):
    try:
        student = request.user.faculty
        return redirect(teacherprofile)

    except:
        student=request.user
    reg_id=request.user
    y = Attendence.objects.filter(Student_ID=reg_id)
    myFilter = StudentFilter(request.GET, queryset=y)
    attendences = myFilter.qs
    context = {'myFilter':myFilter, 'attendences': attendences, 'ta':False}
    return render(request, 'Attendence_Sys/MyAttendence.html', context)



@login_required(login_url='teacherlogin')
def AttendenceReports(request):
    try:
        student = Student.objects.get(registration_id = request.user)
        return redirect(studentprofile)

    except:
        student=request.user
    reports=Reports.objects.all()
    myFilter=ReportFilter(request.GET, queryset=reports)
    reports=myFilter.qs
    context = {'myFilter':myFilter, 'reports': reports, 'ta':False}
    return render(request,'Attendence_Sys/AttendenceReports.html',context)



@login_required(login_url='teacherlogin')
def Defaulters(request):
    try:
        student = Student.objects.get(registration_id = request.user)
        return redirect(studentprofile)

    except:
        student=request.user
    reports=Reports.objects.filter(percentage__lte=50)
    myFilter=ReportFilter(request.GET, queryset=reports)
    reports=myFilter.qs
    context = {'myFilter':myFilter, 'reports': reports, 'ta':True}
    return render(request,'Attendence_Sys/AttendenceReports.html',context)

    

                    
                    
            

def facultyProfile(request):
    try:
        student = Student.objects.get(registration_id = request.user)
        return redirect(studentprofile)

    except:
        student=request.user
    faculty=request.user.faculty
    form = FacultyForm(instance = faculty)
    context = {'form':form}
    return render(request, 'Attendence_Sys/facultyForm.html', context)


def studentlogin(request):
    if request.user.is_authenticated:
        return redirect('studentprofile')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('studentprofile')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'Attendence_Sys/studentlogin.html', context)

@login_required(login_url='studentlogin')
def studentprofile(request):
    try:
        student = request.user.faculty
        return redirect(teacherprofile)

    except:
        student=request.user
    return render(request,'Attendence_Sys/studentprofile.html')



@login_required(login_url='login')
def teacherprofile(request):
    try:
        student = Student.objects.get(registration_id = request.user)
        return redirect(studentprofile)

    except:
        student=request.user
    return render(request,'Attendence_Sys/teacherprofile.html')



@login_required(login_url='login')
def SearchAttendence(request):
    try:
        student = Student.objects.get(registration_id = request.user)
        return redirect(studentprofile)

    except:
        student=request.user
    return render(request,'Attendence_Sys/SearchAttendence.html')



@login_required(login_url='login')
def TakeAttendence(request):
    try:
        student = Student.objects.get(registration_id = request.user)
        return redirect(studentprofile)

    except:
        student=request.user
    return render(request,'Attendence_Sys/TakeAttendence.html')



def UpdateStudent(request):
    try:
        student = request.user.faculty
        return redirect(teacherprofile)

    except:
        student=request.user
    return render(request,'Attendence_Sys/UpdateStudent.html')





@login_required(login_url = 'studentlogin')
def studentlogout(request):
    logout(request)
    return redirect('studentlogin')

# class VideoCamera(object):
#     def __init__(self):
#         self.video = cv2.VideoCapture(0)
#     def __del__(self):
#         self.video.release()

#     def get_frame(self):
#         ret,image = self.video.read()
#         ret,jpeg = cv2.imencode('.jpg',image)
#         return jpeg.tobytes()


# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         yield(b'--frame\r\n'
#         b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


# @gzip.gzip_page
# def videoFeed(request):
#     try:
#         return StreamingHttpResponse(gen(VideoCamera()),content_type="multipart/x-mixed-replace;boundary=frame")
#     except:
#         print("aborted")

# def getVideo(request):
#     return render(request, 'attendence_sys/videoFeed.html')