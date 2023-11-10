from flask import Flask
app = Flask(__name__)
# to run the server you have to cd to the app directory and send the $env:FLASK_APP = "app.py" command in the cmd line then you type flask run command to get the server running

def make_bold(function):
    def wrapper_func():
        return "<b>" + function() + "</b> "
    return  wrapper_func

@app.route('/')
@make_bold
def hello_world():
    return '<h1 style="text-align: center">Hello World!</h1>'\
    '<p>Testing paragraph.</p>'\
    '<img src="https://i.redd.it/yr0rfg3eaqxb1.gif" width=400>'\

@app.route('/bye')
def bye():
    return "bye"

@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello there {name} you are {number} years old!"

if __name__ == "__main__": 
    app.run(debug=True) # Turn on debug mode
