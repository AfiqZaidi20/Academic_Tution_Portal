from django.contrib import admin
from .models import Student, Tutor, Subject, Classinfo, Attendance

# Register your models here.
admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(Subject)
admin.site.register(Classinfo)
admin.site.register(Attendance)