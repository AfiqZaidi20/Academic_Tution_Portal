from django.db import models

# Create your models here.


class Tutor(models.Model):
    tutorid=models.CharField(max_length=15, primary_key=True)
    tutorname=models.TextField(max_length=100)
    tutorno=models.CharField(max_length=15)
    tutorpassword=models.CharField(max_length=8, default='afiq123')

class Student(models.Model):
    studentid=models.CharField(max_length=15, primary_key=True)
    studentname=models.TextField(max_length=100)
    studentno=models.CharField(max_length=15)
    parentno=models.CharField(max_length=15)
    studentpassword=models.CharField(max_length=8, default='afiq123')
    tutorid=models.ForeignKey(Tutor, on_delete=models.CASCADE, null=True)
    
class Subject(models.Model):
    subjectcode=models.CharField(max_length=15, primary_key=True)
    tutorid=models.ForeignKey(Tutor, on_delete=models.CASCADE, null=True)
    subjectname=models.TextField(max_length=100)
    totalhour=models.IntegerField()

class Classinfo(models.Model):
    classcode=models.CharField(max_length=15, primary_key=True)
    classhour=models.IntegerField()
    subjectcode=models.ForeignKey(Subject, on_delete=models.CASCADE, null=True) 
    tutorid=models.ForeignKey(Tutor, on_delete=models.CASCADE, null=True)

class Attendance(models.Model):
    attendanceid=models.CharField(max_length=15, primary_key=True)
    classcode=models.ForeignKey(Classinfo, on_delete=models.CASCADE, null=True)
    studentid=models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    status=models.TextField(max_length=100)

