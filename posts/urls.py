from django.urls import path
from posts.views import post_created, post_list

app_name = 'posts'

urlpatterns = [
    path('create', post_created, name='post-create'),
    path('', post_list, name='post_list'),
]