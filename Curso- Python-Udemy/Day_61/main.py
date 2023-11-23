from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email
from flask_bootstrap import Bootstrap5
from password_gen import pass_gen # My custom Class

#----------------------------- define the password len check ------------------------------
def pass_len(password, field):
    if len(field.data) < 8:
        raise ValidationError('Password must be at least 8 characters')
#----------------------------- create the login form ---------------------------
class loginForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), pass_len])
    submit = SubmitField(label='Log In')

#----------------------------------------------------------------
key = pass_gen.ranGenerator() # auto generated Key
app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = key # Csrf Token Secret
#----------------------------------------------------------------
@app.route("/")
def home():
    return render_template('index.html')
#----------------------------------------------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = loginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    
    return render_template('login.html', form=login_form)
#----------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
