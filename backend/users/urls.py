from django.urls import path
from .views import *

urlpatterns = [
    path('get_refresh_token/',get_user_tokens, name='get_tokens'),
    path('admin-signup/', Admin_Signup.as_view(),name='admin-signup'),
    path('user-signup/',User_Signup.as_view(),name='user-signup'),
    path('login/',login.as_view(),name='user-login'),
    # path('logout/',logout.as_view(),name='logout'),
]
