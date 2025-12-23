from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('students.urls')),
    path('/admin-panel',include('admin_panel.urls')),
    path('/adviser-panel',include('adviser_pannel.urls')),
    path('/users',include('users.urls')),
]
