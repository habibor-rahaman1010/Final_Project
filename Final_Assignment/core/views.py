from django.shortcuts import render, redirect

# Create your views here.
def homeView(request):
    return render(request, 'index.html')