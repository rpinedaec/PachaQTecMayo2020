# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class todo_list(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return  self.name

class todo_item(models.Model):
    list_id = models.ForeignKey(todo_list)
    name = models.CharField(max_length=32)
    content = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return "(%s)%s"%(self.list_id__name,self.name)

    def __unicode__(self):
        return "(%s)%s"%(self.list_id__name,self.name)



