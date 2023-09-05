from django.shortcuts import redirect, render, get_object_or_404
from .models import Author, Category, Article
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from . import forms

# Articale_details functionality here....
def show_All_Blogs(request):
    author = Author.objects.all()
    aritcle = Article.objects.all()
    paginator = Paginator(aritcle, 8) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    tottal_article = paginator.get_page(page_number)

    context = {
        'author': author,
        'aritcle': tottal_article,
    }
    return render(request, 'all_blogs.html', context)

@login_required(login_url='login')
def Article_Details(request, id, slug):
    author = Author.objects.all()
    post = get_object_or_404(Article, pk = id, slug = slug)

    context = {
        'post': post,
        'author': author
    }
    return render(request, 'articles_details.html', context)


# Perticuler article category functionality here....
def Category_Post(request, name):
    author = Author.objects.all()
    aritcle = Article.objects.all()
    cat = get_object_or_404(Category, name=name)
    post = Article.objects.filter(category=cat.id)

    paginator = Paginator(post, 3) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    tottal_article = paginator.get_page(page_number)

    
    context = {
        'author': author,
        'aritcle': aritcle,
        'post': tottal_article,
        'cat': cat
    }
    return render(request, 'category.html', context)

# Create_article frome here......
@login_required(login_url='login')
def ArticlaeFrom(request):
    form = forms.Create_Artical()

    if request.method == "POST":
        form = forms.Create_Artical(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index')

    context = {
        "form": form
    }
    return render(request, 'createArticle.html', context)


# website category show functionality....
def Show_Category(request):
    category = Category.objects.all()
    context = {
        'category': category,
    }
    return render(request, 'show_category.html', context)


#create a author functionality here....
def Create_Author(request):
    form = forms.User_Create_Author()

    if request.method == "POST":
        form = forms.User_Create_Author(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save(commit=True)
            return redirect('create-article')
    context = {
        "form": form
    }
    return render(request, 'create_author.html', context)