from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, MetaData, Table
from application import db, application
from application.models import drinkers, bars
from application.forms import stateSelection, mediaSelection

application.secret_key = 'my336DbProject'

@application.route('/', methods=['GET', 'POST'])
@application.route('/index', methods=['GET', 'POST'])
def index():
    engine = create_engine('mysql+pymysql://my336Db:zohaibdatabase@my336instance.cffs7lx8bqq2.us-east-1.rds.amazonaws.com:3306/BarBeerDrinkerPlus', convert_unicode=True)
    connection = engine.connect()
    state_select = stateSelection(request.form)
    media_select = mediaSelection(request.form)

    if request.method == 'POST' and state_select.validate_on_submit():
        print "state here"
        target_state = state_select.state.data
        bar_tuples=connection.execute("select * from bars where state='"+target_state+"'" ).fetchall()
        drinker_tuples=connection.execute("select * from drinkers where state='"+target_state+"'" ).fetchall()
        return render_template('results.html', results1 = bar_tuples, results2 = drinker_tuples)

    if request.method == 'POST' and media_select.validate_on_submit():
        print "media here"
        target_drinker = media_select.drinker.data
        target_media = media_select.media.data
        friend_tuples= connection.execute("select d.* from friends f join drinkers d on  f.friend_id = d.id where f.drinker_id=" +target_drinker+" and socialmedia_id="+target_media).fetchall()
        print "after friend"
        for row in friend_tuples:
            print (row.name)
        bar_tuples= connection.execute("select b.* from friends f join frequents f1 on f1.drinker_id=f.friend_id join bars b on f1.bar_id=b.id where f.drinker_id="+target_drinker+" and socialmedia_id="+target_media).fetchall()
        print "after bar"
        for row in bar_tuples:
            print (row.name)
        print (here)
        return render_template('results.html', results1 = bar_tuples, results2 = friend_tuples)

    return render_template('index.html', form1 = state_select, form2 = media_select)

if __name__ == '__main__':
    application.run(debug = True)
