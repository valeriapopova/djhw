from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, ArticleTag


class ArticleTagInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            for k, v in form.cleaned_data.items():
                if k == 'is_main' and v is True:
                    counter += 1
        if counter > 1:
            raise ValidationError('Основным может быть только один раздел')
        elif counter < 1:
            raise ValidationError('Укажите основной раздел')
        return super().clean()


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    formset = ArticleTagInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text']
    inlines = [ArticleTagInline, ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
