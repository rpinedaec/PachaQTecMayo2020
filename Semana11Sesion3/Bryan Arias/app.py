from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
#from flask_ngrok import run_with_ngrok
#from flas_http_response import 
import logging


app = Flask(__name__)
#run_with_ngrok(app)


@app.route('/', methods=['POST'])
def inicio():
    app.logger.info('Procesando por defecto el request')
    #data = request.args.to_dict[flat=False]
    app.logger.debug(request.form.get('Body'))
    #incoming_msg = request.POST['body'].lower()
    resp = MessagingResponse()
    msg = resp.message()
    msg.body('Respuesta desde python')
    return str(resp)

@app.route('/', methods=['GET'])
def hello():
    
    return "Hola a todos."


if __name__ == '__main__':
    app.run()
