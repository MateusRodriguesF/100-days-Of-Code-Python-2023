from flask import Flask
import random
#----------------------------------------------------------------
app = Flask(__name__)

number = random.randint(0,10)

#----------------------------------------------------------------
@app.route('/index/')
def index():
    return '<h1 style="text-align: left">Guess a number between 0 and 9</h1>'\
    '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'\
    '<br>'\
#----------------------------------------------------------------
@app.route('/index/<int:usr_num>')
def index_num(usr_num):
    global number
    if usr_num == number - 2:
         return '<h1 style="text-align: left; color:red">Too Low, try again!</h1>'\
    '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'\
    '<br>'\

    elif usr_num == number + 2:
         return '<h1 style="text-align: left; color:blue">Too High, try again!</h1>'\
    '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.g">'\
    '<br>'\
    
    elif usr_num != number: 
         return '<h1 style="text-align: left; color:red">keep trying!</h1>'\
    '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'\
    '<br>'\
    
    else:
        number = random.randint(0, 10)
        print('<h1 style="text-align: left; color:yellow">You found me!</h1>'
        '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')
    
       


#----------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)