from django.contrib import admin
from .import models

# Register your models here.
class SkillAdmin(admin.ModelAdmin):
    list_display = ['html', 'css', 'javascript', 'react', 'express', 'Cprogram', 'Cplus', 'CSharp', 'asp_dotnet_core']

admin.site.register(models.cvModel)
admin.site.register(models.MySkills, SkillAdmin)
