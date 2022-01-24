from django.contrib import admin

from .models import Article, Tag, ArticleTag

class ArticleTagInline(admin.TabularInline):
    model =

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
