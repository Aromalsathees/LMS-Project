from django.urls import path
from .views import *

urlpatterns = [

    path('/get-student-course',GetStudentCourses.as_view(),name='student-course'),
    path('/courses' ,Enroll_Courses.as_view(),name='coursess'),
    path('/enroll-courses',Get_Enrolled_Courses.as_view(),name='enroll-courses')
]


