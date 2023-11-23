from flask import Flask, render_template, redirect, url_for, request,  Markup
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
# import json
import requests


#------------------------------App config------------------------------
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
#------------------------------Forms------------------------------
class EditForm(FlaskForm):
    rating_label = Markup("<b>Your rating out of 10 e.g.7.5</b>")
    review_label = Markup("<b>Your Review</b>")
    rating = StringField(rating_label, validators=[DataRequired()])
    review = StringField(review_label, validators=[DataRequired()])
    submit = SubmitField("Done")

class AddForm(FlaskForm):
    title_label = Markup("<b>Movie Title</b>")
    title = StringField(title_label)
    submit = SubmitField("Add Movie")

#------------------------------Database Configurations------------------------------
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie_ranking.db"
db = SQLAlchemy()
db.init_app(app)
#------------------------------Database Parameters------------------------------
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250),nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250),nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Movie {self.title}>'
with app.app_context():
    db.create_all()
#------------------------------Section App Routes------------------------------
#------------------------------Home Code------------------------------
@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all() # convert ScalarResult to Python List

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", movies=all_movies)

#------------------------------Add Movie Code------------------------------
@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()
    movie_title = form.title.data
    API_KEY = "YourAPIKey"
    API_ENDPOINT = 'https://api.themoviedb.org/3/search/movie'
    params = {
        "query":movie_title,
        "api_key":API_KEY   
    }
    response = requests.get(url=API_ENDPOINT, params=params)
    response.raise_for_status()
    data = response.json()["results"]

    if form.validate_on_submit():
        
        return render_template("select.html", movie_title=movie_title, data=data)

    return render_template("add.html", form=form)

#------------------------------Edit Movie Code------------------------------
@app.route("/edit", methods=["GET", "POST"])
def edit_movie():
    form = EditForm()
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)
#------------------------------Delete Movie Code------------------------------
@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))
#------------------------------Select Movie Code------------------------------
@app.route("/select")
def select():
    movie_id = request.args.get('id')
    if movie_id == "":
        return render_template("select.html")
    else:
        API_KEY = "YourAPIKey"
        API_ENDPOINT = f'https://api.themoviedb.org/3/movie/{movie_id}'
        params = {
            "api_key":API_KEY   
        }
        response = requests.get(url=API_ENDPOINT, params=params)
        response.raise_for_status()
        data = response.json()
        
        title = data["original_title"]
        year = int(data["release_date"][:-6])
        description = data["overview"]
        img_url = "https://image.tmdb.org/t/p/original/"+data["poster_path"]

        new_movie = Movie(
            title = title,
            year = year,
            description = description,
            rating=7.3,
            ranking=10,
            review="My favourite character was the caller.",
            img_url=img_url
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit_movie', id=new_movie.id))

#------------------------------Section App Routes End------------------------------

if __name__ == '__main__':
    app.run(debug=True)

#------------------------------Old Data insertion Code------------------------------
# with app.app_context():
#     new_movie = Movie(
#     id=1,
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# with app.app_context():
#     second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )
#     db.session.add(second_movie)
#     db.session.commit()

