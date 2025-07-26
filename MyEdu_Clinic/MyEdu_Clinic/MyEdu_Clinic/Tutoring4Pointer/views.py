from multiprocessing import context
from django.shortcuts import render, redirect
from Tutoring4Pointer.models import Student, Tutor, Subject, Classinfo, Attendance 
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, get_object_or_404
from .models import Student

# Create your views here.

def home(request):
    return render(request,"home.html")

def home2(request):
    return render(request,"home2.html")

def home3(request):
    return render(request,"home3.html")

def studentlogin(request):
    if request.method == 'POST':
        studentid = request.POST.get('studentid')

        try:
            student = Student.objects.get(studentid=studentid)
            request.session['studentid'] = student.studentid 
            return HttpResponseRedirect(reverse('home2'))  # Redirect to the home page
        except Student.DoesNotExist:
            messages.error(request, 'Invalid student ID')

    return render(request, 'studentlogin.html')  # Adjust the path if necessary

def tutorlogin(request):
    if request.method == 'POST':
        tutorid = request.POST.get('tutorid')

        try:
            tutor = Tutor.objects.get(tutorid=tutorid) 
            request.session['tutorid'] = tutor.tutorid 
            return HttpResponseRedirect(reverse('home3'))  # Redirect to the home page
        except Student.DoesNotExist:
            messages.error(request, 'Invalid student ID')

    return render(request, 'tutorlogin.html')  # Adjust the path if necessary


def updatestudent(request,studentid):
    updateid=Student.objects.get(studentid=studentid)
    dict={
        'updateid':updateid,
        'message':'JUST OPEN PAGE'
    }
    return render(request,"updatestudent.html",dict)

def updatedata(request,studentid,):#tekan button update
    data=Student.objects.get(studentid=studentid)
    stuno1=request.POST['studentno']
    parno1=request.POST['parentno']
    data.studentno=stuno1 #kena letak dua dua text box walaupun kita nak update satu je sebab tak boleh post satu je
    data.parentno=parno1
    data.save()

    return HttpResponseRedirect(reverse("registerstudent"))

def updatetutor(request, tutorid):
    updateid=Tutor.objects.get(tutorid=tutorid)
    dict={
        'updateid':updateid,
        'message':'JUST OPEN PAGE'
    }
    return render(request,"updatetutor.html",dict)

def updatedata(request,tutorid):#tekan button update
    data=Tutor.objects.get(tutorid=tutorid) 
    tutno1=request.POST['tutorno'] 
    data.tutorno=tutno1   #kena letak dua dua text box walaupun kita nak update satu je sebab tak boleh post satu je
    data.save()
    return HttpResponseRedirect(reverse("registertutor"))


def deletestudent(request,studentid):
    deleteid=Student.objects.get(studentid=studentid)
    dict={
        'deleteid':deleteid,
    }
    return render(request,"deletestudent.html",dict)

def deletedata(request,studentid,):#tekan button DELETE
    data=Student.objects.get(studentid=studentid)
    data.delete()
    return HttpResponseRedirect(reverse("registerstudent"))



def deletetutor(request,tutorid):
    deleteid=Tutor.objects.get(tutorid=tutorid)
    dict={
        'deleteid':deleteid,
    }
    return render(request,"deletetutor.html",dict)

def deletedata(request,tutorid,):#tekan button DELETE
    data=Tutor.objects.get(tutorid=tutorid)
    data.delete()
    return HttpResponseRedirect(reverse("registertutor"))



def registerstudent(request):
    stututor1 = Student.objects.all()
    mytutor = Tutor.objects.all()
    
    if request.method == 'POST':
        stuid1 = request.POST['studentid']
        stuname1 = request.POST['studentname']
        stuno1 = request.POST['studentno']
        parno1 = request.POST['parentno']
        tutid1 = request.POST['selecttutid']

        # Check if student ID already exists
        if Student.objects.filter(studentid=stuid1).exists():
            # If the student exists, return an error message
            context = {
                'stututor1': stututor1,  # Students list for table display
                'mytutor': mytutor,  # Mentors list for dropdown
                'message': f"Student with ID {stuid1} already exists!",  # Error message
            }
            return render(request, "registerstudent.html", context)
        else:
            # Assuming Tutor model has 'tutorid' as the primary key
            tutornew = Tutor.objects.get(tutorid=tutid1)

            # Save student data if ID is unique
            data = Student(
                studentid=stuid1, 
                studentname=stuname1, 
                studentno=stuno1, 
                parentno=parno1, 
                tutorid=tutornew
            )
            data.save()

            # Success message
            context = {
                'stututor1': stututor1,  # Students list for table display
                'mytutor': mytutor,  # Mentors list for dropdown
                'message': 'New student has been successfully registered!',
            }
            return render(request, "registerstudent.html", context)
    
    # GET request (when the page is refreshed)
    context = {
        'stututor1': stututor1,  # Students list for table display
        'mytutor': mytutor,  # Mentors list for dropdown
        'message': 'PAGE IS REFRESHED',
    }
    return render(request, 'registerstudent.html', context)


def registertutor(request):
    displaydata= Tutor.objects.all().values()
    if request.method=='POST':
        tutid1=request.POST['tutorid']
        tutname1=request.POST['tutorname']
        tutno1=request.POST['tutorno']
        data=Tutor(tutorid=tutid1, tutorname=tutname1, tutorno=tutno1)
        data.save()

        context={
            'displaydata': displaydata,
            'message': 'hi'

        }

        return render(request,"registertutor.html",context)
    else:
        dict={
            'message':'',
            'displaydata':displaydata,
        }
    return render(request, 'registertutor.html', dict)
