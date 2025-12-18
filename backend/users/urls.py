from django.urls import path

urlpatterns = [
    path('/admin-signup', Admin_signup.as_view(),name='admin-signup'),
    path('/user-signup',User_signup.as_view(),name='user-signup'),
    path('/login',login.as_view(),name='user-login'),
    path('/logout',logout.as_view(),name='logout'),
]
