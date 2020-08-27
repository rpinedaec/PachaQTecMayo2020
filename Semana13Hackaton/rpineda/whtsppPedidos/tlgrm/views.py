from django.shortcuts import render
import json
import os

import requests
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from pdds.models import cliente, pedido

from django.views import generic

# Create your views here.
TELEGRAM_URL = "https://api.telegram.org/bot"
BOT_TOKEN = '1398610721:AAFxcyYIOGJ26K6Nwx36v1mJ2f2w_C5svfU'



class botView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        t_data = json.loads(request.body)
        t_message = t_data["message"]
        t_chat = t_message["chat"]

        try:
            text = t_message["text"].strip().lower()
        except Exception as e:
            return JsonResponse({"ok": "POST request processed"})

        text = text.lstrip("/")

        if text == "menu":
            msg = f"Escribe las siguientes opciones:\n"
            msg += "buscar -> busca tu pedido \n"
            msg += "status <idPedido> -> encuentra es status de tu pedido"
            self.send_message(msg, t_chat["id"])
        elif text == "buscar":
            msg = "Escribe tu DNI en el siguiente formato DNI:12345678"
            self.send_message(msg, t_chat["id"])
        elif text.startswith('dni'):
            dni = text.replace('dni:', '')
            dni = dni.strip() 
            msg = f"Tu dni es {dni}"
            data = self.buscarPedidosPorDocumento(dni)
            strdata = json.dump( {"data": list(data)})
            self.send_message(msg, t_chat["id"])
        elif text == "restart":
            msg = "The Tutorial bot was restarted"
            self.send_message(msg, t_chat["id"])
        else:
            msg = "Bienvenido a SocialPedidos escribe MENU para empezar"
            self.send_message(msg, t_chat["id"])

        return JsonResponse({"ok": "POST request processed"})

    def get(self, request, *args, **kwargs):
        return JsonResponse({"ok": "POST request processed"})

    @staticmethod
    def buscarPedidosPorDocumento(dni):
        miCliente = cliente.objects.all().filter(documento=dni)
        miPedido = pedido.objects.filter(cliente=miCliente)
        return miPedido

    @staticmethod
    def send_message(message, chat_id):
        data = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "Markdown",
        }
        response = requests.post(
            f"{TELEGRAM_URL}{BOT_TOKEN}/sendMessage", data=data
        )