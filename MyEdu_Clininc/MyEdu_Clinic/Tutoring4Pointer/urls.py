from django.urls import path
from . import views
from .views import deletestudent, deletedata, updatedata, updatestudent

urlpatterns = [
    # Home and login paths
    path("", views.home, name="home"),
    path("home2/", views.home2, name="home2"),
    path("home3/", views.home3, name="home3"),
    path('studentlogin/', views.studentlogin, name='studentlogin'),
    path('tutorlogin/', views.tutorlogin, name='tutorlogin'),

    path("updatestudent", views.updatestudent, name="updatestudent"),
    path("updatestudent/updatedata/<str:studentid>", views.updatedata, name="updatedata"),
    
    
    path("updatetutor", views.updatetutor, name="updatetutor"),
    path("updatetutor/updatedata/<str:tutorid>", views.updatedata, name="updatedata"),
    

    path('registerstudent', views.registerstudent, name='registerstudent'),
    path('registertutor', views.registertutor, name='registertutor'),
    path("deletestudent", views.deletestudent, name="deletestudent"),
    path("deletetutor", views.deletetutor, name="deletetutor"),  
    
    
    path('deletestudent/<int:tutorid>/', views.deletestudent, name='deletestudent'),
    path('deletedata/<int:tutorid>/', views.deletedata, name='deletedata'),
    path('updatestudent/<str:studentid>/', views.updatestudent, name='updatestudent'),
    path('updatestudent/updatedata/<str:stuid>/', views.updatedata, name='updatedata'),
    path("deletestudent/", views.deletestudent, name="deletestudent"),


]