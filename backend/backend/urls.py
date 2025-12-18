from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('students.urls')),
    path('/admin-pannel',include('admin_pannel.urls')),
    path('/adviser-pannel',incluce('adviser-pannel.urls')),
    path('/users',include('users.urls')),
]
