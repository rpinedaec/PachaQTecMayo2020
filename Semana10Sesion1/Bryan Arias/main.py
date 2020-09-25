from flask import Flask
from 

app = Flask(__name__)

@app.route('/<user>')

def inicio(user):
    return "Hellos %s" #% escape(user)

if __name__ == '__main__':
    app.run()