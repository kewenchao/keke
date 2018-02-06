# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True, max_length=64, verbose_name='主键id')
    name = models.CharField(max_length=64,verbose_name='姓名', null=True)
    pwd = models.CharField(max_length=64,verbose_name='密码', null=True)
    class Meta:
        verbose_name = '人员表'
        verbose_name_plural = verbose_name
        db_table = 'user'