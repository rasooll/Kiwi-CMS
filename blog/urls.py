from django.urls import path

from . import views

urlpatterns = [
    path(
        '',
        views.index,
        name='index'
        ),
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
    path(
        '<slug:slug>/',
        views.view_page,
        name='view_other_page'
    ),
    path(
        'page/<int:number>',
        views.Pagination,
        name='view_pagination'
    ),
    path(
        'user/register/',
        views.user_registration,
        name='user_registeration'
    )
]