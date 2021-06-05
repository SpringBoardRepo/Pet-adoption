
from flask import Flask, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import Pet, connect_db
from forms import AddPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://localhost/pet?user=postgres&password=postgresql'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

# debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def home_page():
    pets = Pet.query.all()
    return render_template('pets.html', pets=pets)


@app.route('/add_pet')
def add_pet():
    form = AddPetForm()

    return render_template('add_pet.html', form=form)
