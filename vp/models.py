from django.db import models


class Person (models.Model):
    MAN = 'M'
    WOMAN = 'Ж'
    SEX = [(MAN ,'Man'),(WOMAN ,'Woman')]
    name = models.CharField(max_length=30,verbose_name='Имя')
    family_name = models.CharField(max_length=30, verbose_name='Фамилия')
    age = models.IntegerField()
    sex = models.CharField(max_length=3,choices=SEX,default=MAN)

    class Meta:
        verbose_name_plural = 'Peoples'
        verbose_name = 'People'
        ordering = ['age']
