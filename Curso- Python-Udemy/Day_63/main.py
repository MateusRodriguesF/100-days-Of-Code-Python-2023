from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5

from flask_sqlalchemy import SQLAlchemy
#------------------------------------------------- App initialize ------------------------------------------------
app = Flask(__name__)
bootstrap = Bootstrap5(app)
#------------------------------------------------- DataBase settings ---------------------------------------------
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///My_library.db" # Create database My_library.db
db = SQLAlchemy() # Call SQLAlchemy 
db.init_app(app) #Initialize database connection
#----------------------------------------------------- Vars ------------------------------------------------------
all_books = []
#------------------------------------------------- DataBase parameters -------------------------------------------
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'
with app.app_context():
    db.create_all()
#------------------------------------------------- Routes ---------------------------------------------------------
@app.route('/')
def home(): 
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    return render_template('index.html',books=all_books)
#------------------------------------------------------------------------------------------------------------------
@app.route("/add", methods=['GET','POST'])
def add():
    if request.method == "POST":
        new_book = Book(
            title = request.form["title"],
            author = request.form["author"],
            rating = float(request.form["rating"])
        )
        # all_books.append(new_book)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add.html')
#------------------------------------------------------------------------------------------------------------------
@app.route('/edit', methods=['GET','POST'])
def edit():
    if request.method == 'POST':
        book_id = request.form["id"]#come from edit.html request
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form["rating"]#come from edit.html request
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Book, book_id)
    return render_template('edit.html', book=book_selected)
#------------------------------------------------------------------------------------------------------------------
@app.route('/delete')
def delete():
    book_id = request.args.get('id')
    
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))
#------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)

#------------------------------------------------------------------------------------------------------------------
#  Old versions of code
# import sqlite3
# db = sqlite3.connect("book_collection.db")
# cursor = db.cursor()
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J.K.Rowling', 9.3)")
# db.commit()