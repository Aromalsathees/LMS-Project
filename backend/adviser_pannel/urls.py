from django.urls import path
from .views import *

urlpatterns = [
    path('/create-course',Create_Course.as_view(),name='course'),
    path('/add-materials', Add_Materials.as_view(),name='materials'),
    path('/adviser-courses',Get_Adviser_courses.as_view(),name='advisecourses')
]
