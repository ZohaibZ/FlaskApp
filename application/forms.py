from flask_wtf import FlaskForm
from application.models import drinkers, bars
from wtforms import TextField, validators, SelectField, SubmitField, SelectMultipleField

STATE_CHOICES = [('AL', 'Alabama'),('AK','Alaska'),('AZ', 'Arizona'),('AR','Arkansas'),('CA','California'),('CO','Colorado'),
                ('CT','Connecticut'),('DE','Delaware'),('FL','Florida'),('GA','Georgia'),('HI','Hawaii'),('ID','Idaho'),
                ('IL','Illinois'),('IN','Indiana'),('IA','Iowa'),('KS','Kansas'),('KY','Kentucky'),('LA','Louisiana'),
                ('ME','Maine'),('MA','Massachusetts'),('MI','Michigan'),('MN','Minnesota'),('MS','Mississippi'),('MO','Missouri'),
                ('MT','Montana'),('NE','Nebraska'),('NV','Nevada'),('NH','New Hampshire'),('NJ','New Jersey'),('NM','New Mexico'),
                ('NY','New York'),('NC','North Carolina'),('ND','North Dakota'),('OH','Ohio'),('OK','Oklahoma'),('OR','Oregon'),
                ('PA','Pennsylvania'),('RI','Rhode Island'),('SC','South Carolina'),('SD','South Dakota'),('TN','Tennessee'),('TX','Texas'),
                ('UT','Utah'),('VT','Vermont'),('VA','Virginia'),('WA','Washington'),('WV', 'West Virginia'),('WI','Wisconsin'),('WY','Wyoming'),
                ('DC','District of Columbia'),('PR','Puerto Rico')]

DRINKER_CHOICES = [(a.id, a.name) for a in drinkers.query.all()]

class stateSelection(FlaskForm):
    state = SelectField(label = 'State', choices = STATE_CHOICES)
    submit_state = SubmitField('Submit')
    
class mediaSelection(FlaskForm):
    drinker = SelectField(label = 'Drinker', choices = DRINKER_CHOICES)
    media = SelectField(label = 'media', choices = [('1', 'facebook'),('2','twitter'),('3','instagram')])
    submit_media = SubmitField('Submit')

class drinkerSelection(FlaskForm):
    state = SelectField()
