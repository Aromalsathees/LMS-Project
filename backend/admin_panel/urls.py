from django.urls import path
from .views import *

urlpatterns = [
    path('/user-details', User_Manager.as_view(),name ='user-manager'),

    path('/course-details',Course_status.as_view(),name ='course-details'),
    path('/delete-course/<int:pk>/',Delete_course.as_view(),name='delete-course'),
    path('/course-count', Course_count.as_view(),name='coure-count'),
    
    path('/enrolled-students-details',Enrolled_students.as_view(),name='students-details')

]
