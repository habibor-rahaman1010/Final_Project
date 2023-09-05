from django.contrib import admin
from .models import ProjectCategory, Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'slug']

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectCategory)