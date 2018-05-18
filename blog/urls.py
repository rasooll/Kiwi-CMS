from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path(
        'post/<slug:slug>/',
        views.view_post,
        name='view_blog_post'
        ),
    path(
        'category/<slug:slug>/',
        views.view_category,
        name='view_blog_category'
        ),
    path(
        'tag/<str:name>/',
        views.view_tags,
        name='view_tags_category'
        ),
]