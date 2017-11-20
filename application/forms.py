from flask_wtf import FlaskForm
from application.models import *
from wtforms import TextField, validators, SelectField, SubmitField, SelectMultipleField, fields
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField

STATE_CHOICES = [('AL', 'Alabama'),('AK','Alaska'),('AZ', 'Arizona'),('AR','Arkansas'),('CA','California'),('CO','Colorado'),
                ('CT','Connecticut'),('DE','Delaware'),('FL','Florida'),('GA','Georgia'),('HI','Hawaii'),('ID','Idaho'),
                ('IL','Illinois'),('IN','Indiana'),('IA','Iowa'),('KS','Kansas'),('KY','Kentucky'),('LA','Louisiana'),
                ('ME','Maine'),('MA','Massachusetts'),('MI','Michigan'),('MN','Minnesota'),('MS','Mississippi'),('MO','Missouri'),
                ('MT','Montana'),('NE','Nebraska'),('NV','Nevada'),('NH','New Hampshire'),('NJ','New Jersey'),('NM','New Mexico'),
                ('NY','New York'),('NC','North Carolina'),('ND','North Dakota'),('OH','Ohio'),('OK','Oklahoma'),('OR','Oregon'),
                ('PA','Pennsylvania'),('RI','Rhode Island'),('SC','South Carolina'),('SD','South Dakota'),('TN','Tennessee'),('TX','Texas'),
                ('UT','Utah'),('VT','Vermont'),('VA','Virginia'),('WA','Washington'),('WV', 'West Virginia'),('WI','Wisconsin'),('WY','Wyoming'),
                ('DC','District of Columbia'),('PR','Puerto Rico')]

MEDIA_CHOICES = [('1','facebook'),('2','twitter'),('3','instagram')]

class stateSelection(FlaskForm):
    state = SelectField(label = 'State', choices = STATE_CHOICES)
    submit = SubmitField("Submit")

def drinker_query():
    return drinkers.query.order_by(drinkers.name)

class mediaSelection(FlaskForm):
    drinker = QuerySelectField(query_factory=drinker_query ,allow_blank=False)
    media = SelectField(label = 'Media', choices = MEDIA_CHOICES)
    submit = SubmitField("Submit")
