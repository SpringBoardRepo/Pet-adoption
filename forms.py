from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.fields.core import BooleanField, StringField


class AddPetForm(FlaskForm):

    name = StringField('Pet Name', [validators.required()])
    species = StringField('Species')
    photo_url = StringField('URL', [validators.optional()])
    age = StringField('Age', [validators.optional()])
    notes = StringField("Notes", [validators.optional()])
    available = BooleanField('Available')
