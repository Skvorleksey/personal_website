from django.db import models


# Create your models here.
class WorkExperienceEntry(models.Model):
    """Describes work experience"""
    company_name = models.CharField(max_length=100, verbose_name='Компания')
    position = models.CharField(max_length=100, verbose_name='Должность')
    start = models.DateField(verbose_name='Начало работы')
    finish = models.DateField(verbose_name='Окончание работы', null=True, blank=True)
    job_duties = models.TextField(verbose_name='Обязанности', blank=True, default='')

    class Meta:
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыт работы'

    def get_finish_date(self):
        if not self.finish:
            return 'по настоящее время'
        return self.finish

    def __str__(self):
        return f'{self.position} в {self.company_name}'


class Skill(models.Model):
    """Skill for cv"""
    name = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.name
