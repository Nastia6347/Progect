# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Rating(models.Model):
    rating = models.IntegerField(u'Оценка')

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценка'

    def __unicode__(self):
        return unicode(self.rating)


class Post(models.Model):
    id_user = models.ForeignKey(User, verbose_name='Пользователь', blank=True, null=True)
    fio = models.CharField(u'Автор отзыва', max_length=255)
    date = models.DateField('Дата публикации')
    id_rating = models.ForeignKey(Rating, verbose_name='Оцека', default='5')
    content = models.TextField(u'Текст отзыва', max_length=10000)
    yes = models.IntegerField(u'Кол-во да', blank=True, null=True)
    no = models.IntegerField(u'Кол-во нет', blank=True, null=True)
    is_active = models.BooleanField(u'Активный?', default=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзыв'

    def __unicode__(self):
        return unicode(self.fio) + " " + unicode(self.content) + " " + unicode(self.date) + " " + unicode(self.id_rating)
