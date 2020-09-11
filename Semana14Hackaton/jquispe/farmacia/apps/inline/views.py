# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView
from django.http import HttpResponseRedirect
from models import *
from forms import *
# Create your views here.

class todo_listListView(ListView):
    model = todo_list
    template_name = 'inline/todo_list.html'

class todo_listUpdateView(UpdateView):
    model = todo_list
    template_name = 'inline/todo_list_update.html'
    success_url = '/todolist/'
    form_class = todo_listForm

    def get_context_data(self, **kwargs):
        context = super(todo_listUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context.update(item_form = todo_itemSet(self.request.POST))
        else:
            context.update(item_form = todo_itemSet(instance =todo_list.objects.get(pk = self.kwargs.get('pk',False))))
        return  context

    def form_valid(self, form):
        iter_form = todo_itemSet(self.request.POST,instance=self.object)
        if iter_form.is_valid():
            self.object = form.save()
            iter_form.instance = self.object
            iter_form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data())

class todo_listCreateView(CreateView):
    model = todo_list
    template_name = 'inline/todo_list_create.html'
    success_url = '/todolist/'
    form_class = todo_listForm

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        item_form = todo_itemSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  item_form=item_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        item_form = todo_itemSet(self.request.POST)
        if (form.is_valid() and item_form.is_valid()):
            self.object = form.save()
            item_form.instance = self.object#why not list_id?
            item_form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(
            self.get_context_data(form=form,
                                  item_form=item_form))


class todo_listDetailsView(DetailView):
    model = todo_list
    template_name = 'inline/todo_list_detail.html'
