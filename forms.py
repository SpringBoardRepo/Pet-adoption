from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.fields.core import BooleanField, SelectField, StringField, IntegerField


class AddPetForm(FlaskForm):

    name = StringField('Pet Name', [validators.required()])
    species = SelectField('Species', [validators.required()], choices=[
                          ('cat', 'Cat'), ('dog', 'Dog'), ("porcupine", "Porcupine")])
    photo_url = StringField('URL', [validators.optional()])
    age = IntegerField('Age', [validators.optional()])
    notes = StringField("Notes", [validators.optional()])
    available = BooleanField('Available')
