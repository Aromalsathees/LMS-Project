from django.urls import path

urlpatterns = [
    path('/add-course', Add_course.as_view(),name ='addcourses')
]
