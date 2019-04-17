from django.db import models

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(null=True, blank=True, verbose_name='Текст')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Заголовки постов'
        verbose_name = 'Пост'
        ordering = ['-published']

