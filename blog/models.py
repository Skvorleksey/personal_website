from django.db import models
from personal_site.settings import AUTH_USER_MODEL


class BlogPost(models.Model):
    publication_date_time = models.DateTimeField(
        verbose_name='Дата и время публикации',
    )
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст поста')
    edited = models.BooleanField(default=False)
    edited_date_time = models.DateTimeField(
        verbose_name='Дата и время изменения',
        auto_now=True,
    )

    class Meta:
        verbose_name = 'Пост в блоге'
        verbose_name_plural = 'Посты в блоге'

    def __str__(self):
        return f'{self.text[:50]}...' if len(self.text) > 50 else self.text
