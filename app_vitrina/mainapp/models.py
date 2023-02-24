from django.db import models


# class Brand(models.Model):
#     name = models.CharField(max_length=16,
#                             unique=True,
#                             verbose_name='название')


class Member(models.Model):
    id = models.AutoField(primary_key=True),
    name = models.CharField(max_length=16,
                            unique=True,
                            verbose_name='имя')
    lastname = models.CharField(max_length=16,
                            unique=True,
                            verbose_name='фамилия')
   
    age = models.PositiveIntegerField(
                                      verbose_name='возраст',
                                     )
  
