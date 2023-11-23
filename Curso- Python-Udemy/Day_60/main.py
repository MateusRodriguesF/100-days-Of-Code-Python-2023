from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    name = request.form['username'].capitalize()
    password = request.form['password']
    return render_template('login.html', name=name, password=password)


if __name__ == '__main__':
    app.run(debug=True)