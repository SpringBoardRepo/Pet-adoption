
from flask import Flask, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import Pet, connect_db, db
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
    """List all the Pets"""
    pets = Pet.query.all()
    return render_template('pets.html', pets=pets)


@app.route('/pet/new', methods=['GET', 'Post'])
def add_pet():
    """Add a new pet"""
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        new_pet = Pet(name=name, species=species, photo_url=photo_url,
                      age=age, notes=notes, available=available)

        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_pet.html', form=form)


@app.route('/view_details/<int:pet_id>')
def view_pet(pet_id):
    """Show Pet Details"""
    pet = Pet.query.get(pet_id)
    return render_template('pet_details.html', pet=pet)


@app.route('/pet/<int:pet_id>/edit', methods=['GET', 'Post'])
def edit_pet(pet_id):
    """Edit a pet"""
    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        return redirect(f'/view_details/{pet.id}')
    else:
        return render_template('add_pet.html', form=form)
