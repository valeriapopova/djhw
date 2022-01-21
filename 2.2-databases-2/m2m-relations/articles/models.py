from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scopes = models.ManyToManyField

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


# class Scope(models.Model):
#
#
#
# class Tag(models.Model):
#     name = models.CharField(max_length=28, verbose_name='Название')
#
#     class Meta:
#         verbose_name = 'Тег'
#         verbose_name_plural = 'Теги'
#
#     def __str__(self):
#         return self.name