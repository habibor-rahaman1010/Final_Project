from django.shortcuts import render, redirect, get_object_or_404
from .models import Project

# Create your views here.
def sgowAllProjects(request):
    project = Project.objects.all()
    return render(request, 'show_all_project.html', context={'project':project})

def detailsProject(request, id, slug):
    data = get_object_or_404(Project, pk = id, slug = slug)
    return render(request, 'show_details_project.html', context={'details': data})