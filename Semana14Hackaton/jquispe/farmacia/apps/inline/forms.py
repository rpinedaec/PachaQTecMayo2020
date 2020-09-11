# -*- coding:utf-8 -*-

from django.forms import ModelForm,Textarea
from models import  *
from django.forms.models import inlineformset_factory,modelform_factory

class todo_listForm(ModelForm):
    class Meta:
        model = todo_list
todo_itemSet = inlineformset_factory(todo_list, todo_item, extra=4)
