from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from flask_http_response import success, result, error
import logging
import requests

app = Flask(__name__)



@app.route('/', methods=['POST'])
def inicio():
    app.logger.info('Processing default request')
    body = request.form.get("Body")
    nroFrom = request.form.get("From")
    app.logger.info(nroFrom)
    if body == 'noticias':
        return sendNoticias()
    elif body == 'perros':
        return sendPerros()
    else:
        return msgDefault()
   # incoming_msg = data.POST['Body'].lower()
    resp = MessagingResponse()
    msg = resp.message()
    msg.body('Mi respuesta desde python flask')
    
    return str(resp)

def msgDefault():
    resp = MessagingResponse()
    msg = resp.message()
    msg.body('Hola bienvenido a mi chatbot escribe *noticias* para verlas; escribe *perros* para verlos')
    return str(resp)
def sendPerros():
    resp = MessagingResponse()
    msg = resp.message()
    r = requests.get('https://dog.ceo/api/breeds/image/random')
    data = r.json()
    #msg.PersistentAction=['geo:37.787890,-122.391664|375 Beale St']
    msg.media(data['message'])
    return str(resp)
def sendNoticias():
    resp = MessagingResponse()
    msg = resp.message()

    r = requests.get('https://deperu.com/api/rest/noticias.json')
    data = r.json()
    i=0
    result = ''
    for obj in data:
        app.logger.debug(obj.get('titulo'))
        titulo = obj.get('titulo')
        url = obj.get('url')
        fecha = obj.get('fecha')
        result += """
        *{}*
        mas: {}
        _Published at {} UTC_
        """.format(
            titulo,
            url, 
            fecha
            )

        i=i+1
        if i == 5:
            break
    
    msg.body(result)
    return str(resp)



@app.route('/', methods=['GET'])
def hello():
    
    return "Hola desde mi maquina RP Sesion 3 de la semana 11"


if __name__ == '__main__':
    app.run()