from django.shortcuts import render

from articles.models import Article, Tag


def articles_list(request):
    template = 'articles/news.html'
    object_list = Article.objects.order_by('-published_at')
    context = {
        'object_list': object_list
    }

    return render(request, template, context)


def tag_detail(request, slug):
    template = 'articles/tag.html'
    tag = Tag.objects.get(slug__iexact=slug)
    context = {
        'tag': tag
    }
    return render(request, template, context)
