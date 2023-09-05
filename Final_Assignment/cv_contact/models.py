from django.db import models

# Create your models here.

class cvModel(models.Model):
    cv_url = models.URLField()

    def __str__(self):
        return self.cv_url

class MySkills(models.Model):
    html = models.IntegerField()
    css = models.IntegerField()
    javascript = models.IntegerField()
    react = models.IntegerField()
    express = models.IntegerField()
    Cprogram = models.IntegerField()
    Cplus = models.IntegerField()
    CSharp = models.IntegerField()
    asp_dotnet_core = models.IntegerField()

    # def __str__(self):
    #     return str(self.CSharp)
    
    