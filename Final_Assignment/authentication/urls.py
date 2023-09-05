from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('password_change/', views.pass_change, name='passchange'),
    path('forgot_pass/', views.forgot_pass, name='forgotpass'),
    path('user_details_change/', views.userDataUpdate, name='userdetailschange'),
]