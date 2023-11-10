from flask import Flask
app = Flask(__name__)
# to run the server you have to cd to the app directory and send the $env:FLASK_APP = "app.py" command in the cmd line then you type flask run command to get the server running
@app.route('/')
def hello_world():
    return "hello world"