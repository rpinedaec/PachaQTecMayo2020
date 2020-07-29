from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola muchachos, los saludo desde Flask'

@app.route('/')
def hello_world():
    return 'Hola muchachos, los saludo desde Flask'