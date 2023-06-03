from django.contrib import admin
from django.urls import path
from . import views
app_name = 'blog_app'

urlpatterns = [
    path('blog_list/', views.blog_list, name='blog_list'),
    path('CreateBlog/',views.CratBlogView.as_view(), name='CreateBlog'),
    path('blog_detail/<slug>/', views.blog_detail,name='blog_detail'),
    path('Liked/<pk>/', views.Liked, name='Liked'),
    path('Unlike/<pk>/', views.Unlike, name='Unlike'),
    path('my_blog/', views.my_blog.as_view(), name='my_blog'),
    path('UdateBlogs/<pk>/', views.UdateBlogs.as_view(), name='UdateBlogs'),
    path('DeleteBlogs/<pk>/', views.DeleteBlogs.as_view(), name='DeleteBlogs'),
    path('follow/<username>/',views.follow, name='follow'),
    path('unfollow/<username>/',views.unfollow, name='unfollow'),


    
    
]
