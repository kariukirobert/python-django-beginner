from django.urls import path
from . import views


urlpatterns = [
    path('', views.getAllBlogs),
    path('<str:slug>/', views.getBlogDetail),
    path('create-new', views.createBlog),
    path('<str:slug>/edit', views.updateBlog),
    path('<str:slug>/delete', views.destroyBlog),
]