from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>hello world</h1>'

#to run in the terminal:  set FLASK_APP=app.py 
#                         flask run