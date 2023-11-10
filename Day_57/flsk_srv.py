from flask import Flask, render_template
import random,datetime,requests

app = Flask(__name__)

@app.route('/')
def get_index():
    #--------------------------- Vars --------------------------------
    td = datetime.date.today()
    year = td.strftime('%Y')
    random_number = random.randint(1, 10)
    autor = "Mateus"
    #----------------------------------------------------------------
    return render_template('index.html',
    num=random_number, 
    year=year, 
    autor=autor
    )
@app.route('/guess/<name>')
def get_guess(name):
    #----------------------------------------------------------------
    parameters = {"name":name}
    age_url = "https://api.agify.io"
    gender_url = "https://api.genderize.io"
    #----------------------------------------------------------------
    age_return = requests.get(url=age_url, params=parameters)
    age_return.raise_for_status()
    age_data = age_return.json()
    #----------------------------------------------------------------
    gender_return = requests.get(url=gender_url, params=parameters)
    gender_return.raise_for_status()
    gender_data = gender_return.json()
    #----------------------------------------------------------------
    age = age_data["age"]
    gender = gender_data["gender"]
    #----------------------------------------------------------------
    return render_template('guess.html',
    name=name.capitalize(),
    age=age,
    gender = gender
    )
@app.route('/blog')
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)








if __name__ == '__main__':
    app.run(debug=True)