from django.urls import path

from articles.views import articles_list, tag_detail

urlpatterns = [
    path('', articles_list, name='articles'),
    path('tag/<str:slug>', tag_detail, name='tag_url'),
]
