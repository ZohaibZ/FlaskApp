from flask_wtf import FlaskForm
from application.models import *
from wtforms import TextField, validators, SelectField, SubmitField, SelectMultipleField, fields
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

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

MONTH_CHOICES = [('9','September'),('10','October'),('11', 'November')]

def drinker_query():
    return drinkers.query.order_by(drinkers.name)

def bar_query():
    return bars.query.order_by(bars.name)

def beer_query():
    return beers.query.order_by(beers.name)

class stateSelection(FlaskForm):
    state = SelectField(label = 'State', choices = STATE_CHOICES)

class mediaSelection(FlaskForm):
    drinker = QuerySelectField(label='Drinker', query_factory=drinker_query ,allow_blank=False)
    media = SelectField(label = 'Media', choices = MEDIA_CHOICES)

class monthlySales(FlaskForm):
    bar = QuerySelectField(label='Bar', query_factory=bar_query, allow_blank=False)
    month = SelectField(label = 'Month', choices = MONTH_CHOICES)

class dailyAvgs(FlaskForm):
    bar1 = QuerySelectField(label = 'Bar', query_factory=bar_query, allow_blank=False)
    month1 = SelectField(label = 'Month', choices = MONTH_CHOICES)

class userLikes(FlaskForm):
    drinker1 = QuerySelectField(label='Drinker', query_factory=drinker_query ,allow_blank=False)
    state1 = SelectField(label = 'State', choices = STATE_CHOICES)

class timeOfDay(FlaskForm):
    state2 = SelectField(label = 'State', choices = STATE_CHOICES)
    month2 = SelectField(label = 'Month', choices = MONTH_CHOICES)

class bartenderAvg(FlaskForm):
    state3 = SelectField(label = 'State', choices = STATE_CHOICES)
    month3 = SelectField(label = 'Month', choices = MONTH_CHOICES)

class typeOfBar(FlaskForm):
    state4 = SelectField(label = 'State', choices = STATE_CHOICES)
    month4 = SelectField(label = 'Month', choices = MONTH_CHOICES)

class whoVisits(FlaskForm):
    state5 = SelectField(label = 'State', choices = STATE_CHOICES)
    month5 = SelectField(label = 'Month', choices = MONTH_CHOICES)

class insertBar(FlaskForm):
    barName = TextField(label='Bar Name', description="enter", validators=[validators.required(), validators.Length(min=0, max=128, message=u'Enter 128 characters or less')])
    barState = SelectField(label = 'State', choices = STATE_CHOICES)

class insertDrinker(FlaskForm):
    drinkerName = TextField(label='Drinker Name', description="enter", validators=[validators.required(), validators.Length(min=0, max=128, message=u'Enter 128 characters or less')])
    drinkerState = SelectField(label = 'State', choices = STATE_CHOICES)

class insertBeer(FlaskForm):
    bar2 = QuerySelectField(label = 'Bar', query_factory=bar_query, allow_blank=False)
    beer2 = QuerySelectField(label = 'Beer', query_factory=beer_query, allow_blank=False)
