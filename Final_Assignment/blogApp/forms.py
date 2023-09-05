from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . import models

class Create_Artical(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = "__all__"


class User_Create_Author(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = "__all__"