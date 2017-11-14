from flask_wtf import Form
from wtforms import TextField, validators

STATE_CHOICES = [('NY', 'New York'),('CA','California'),('IL', 'Illinois'),('TX','Texas'),
                ('AZ', 'Arizona'),('PA', 'Pennsylvania'),('FL','Florida'), ('OH','OHIO'),
                ('IN','Indiana'),('NC', 'North Carolina'),('WA', 'Washington'),('CO', 'Colorado')]

class MyForm(wtforms.Form):
    state = wtforms.SelectField(label='State', choices=STATE_CHOICES)
