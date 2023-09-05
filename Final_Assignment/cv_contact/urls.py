from django.urls import path
from . import views 


urlpatterns = [
    path('conatct/', views.get_conatact, name='conatct'),
    path('skills/', views.my_skills, name='skills'),
]