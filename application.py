from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, MetaData, Table
from application import db, application
from application.models import drinkers, bars
from application.forms import stateSelection, mediaSelection, drinkerSelection

application.secret_key = 'my336DbProject'

@application.route('/', methods=['GET', 'POST'])
@application.route('/index', methods=['GET', 'POST'])
def index():
    engine = create_engine('mysql+pymysql://my336Db:zohaibdatabase@my336instance.cffs7lx8bqq2.us-east-1.rds.amazonaws.com:3306/BarBeerDrinkerPlus', convert_unicode=True)
    connection = engine.connect()

    state_select = stateSelection(request.form)
    media_select = mediaSelection(request.form)

    if request.method == 'POST' and state_select.validate_on_submit():
        target_state = state_select.state.data
        bar_tuples=connection.execute("select * from bars where state='"+target_state+"'" ).fetchall()
        drinker_tuples=connection.execute("select * from drinkers where state='"+target_state+"'" ).fetchall()
        return render_template('results.html', results1 = bar_tuples, results2 = drinker_tuples)

    return render_template('index.html', form1 = state_select, form2 = media_select)

if __name__ == '__main__':
    application.run(debug = True)
