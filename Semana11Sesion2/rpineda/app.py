from flask import Flask, request
from flask_ngrok import run_with_ngrok
app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run


@app.route('/', methods=['POST'])
def inicio():
    req = request.get_json()
    return req

@app.route('/', methods=['GET'])
def hello():
    
    return "Hola desde mi maquina RP"


if __name__ == '__main__':
    app.run()