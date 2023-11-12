from flask import Flask, render_template
import requests
from datetime import date

today = date.today()
act_date = today.strftime("%d/%m/%Y")
year = today.strftime('%Y')

response = requests.get(url="https://api.npoint.io/0b1d217ea418404136d2")
posts = response.json()

app = Flask(__name__)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route('/')
def index():
    return render_template('index.html', all_posts=posts, act_date=act_date, year=year, show_post=show_post)

@app.route('/about.html')
def about():
    return render_template('about.html', year=year)

@app.route('/contact.html')
def contact():
    return render_template('contact.html', year=year)

if __name__ == '__main__':
    app.run(debug=True)