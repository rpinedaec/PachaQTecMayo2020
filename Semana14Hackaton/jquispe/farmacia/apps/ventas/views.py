from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from .models import *
from .forms import *



class todo_listCreateView(CreateView):
    model = Cabecera_Venta
    template_name = 'venta/todo_list_create.html'
    #success_url = '/todolist/'
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


def TodoitemAjax(request):
    if request.is_ajax():
        autor = todo_item.objects.get(id = request.GET['id'])
        response = JsonResponse({'medicamento': autor.medicamento, 'cantidad': autor.cantidad})
        return HttpResponse(response.content)
    else:
        return redirect('/')
