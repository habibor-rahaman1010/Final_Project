from django.urls import path
from . import views 


urlpatterns = [
    path('all_blogs/', views.show_All_Blogs, name = 'All_Blogs'),    
    path('article/<int:id>/<slug:slug>/', views.Article_Details, name = 'article_details'), 
    path('category/<name>', views.Category_Post, name="category"),
    path('create-article/', views.ArticlaeFrom, name = 'create-article'),
    path('show_category/', views.Show_Category, name = 'show_category'),
    path('create_author/', views.Create_Author, name = 'create_author')
]