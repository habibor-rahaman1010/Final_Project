from django.shortcuts import render
from .import models

# Create your views here.
def get_conatact(request):
    return render(request, 'contact.html')

def my_skills(request):
    data = models.MySkills.objects.all()
    return render(request, 'skills.html', context={'data': data})