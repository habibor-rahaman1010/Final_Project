from django.db import models
from django.utils.text import slugify

# Create your models here.
class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    screenshots = models.ImageField(upload_to='project_screenshots/')
    technologies_used = models.CharField(max_length=200)
    project_url = models.URLField()
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, unique=True, null=True, blank=True, allow_unicode=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify([str(self.title), self.category])
        super(Project, self).save(*args, **kwargs)