from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, MetaData, Table
from application import db, application
from application.models import *
from application.forms import *

application.secret_key = 'my336DbProject'

@application.route('/', methods=['GET', 'POST'])
@application.route('/index', methods=['GET', 'POST'])
def index():
    engine = create_engine('mysql+pymysql://my336Db:zohaibdatabase@my336instance.cffs7lx8bqq2.us-east-1.rds.amazonaws.com:3306/BarBeerDrinkerPlus', convert_unicode=True)
    connection = engine.connect()

    state_select = stateSelection(request.form)
    media_select = mediaSelection(request.form)
    monthly_sale = monthlySales(request.form)
    daily_avgs = dailyAvgs(request.form)
    user_likes = userLikes(request.form)

    if request.method == 'POST' and state_select.validate_on_submit():
        print "state here"
        target_state = state_select.state.data
        bar_tuples=connection.execute("select * from bars where state='"+target_state+"'" ).fetchall()
        drinker_tuples=connection.execute("select * from drinkers where state='"+target_state+"'" ).fetchall()
        return render_template('results1.html', results1 = bar_tuples, results2 = drinker_tuples)

    if request.method == 'POST' and user_likes.validate_on_submit():
        print "user here"
        target_drinker = user_likes.drinker1.data
        target_state = user_likes.state1.data
        bar_tuples=connection.execute("select distinct b.* from likes l join sells s on l.beer_id = s.beer_id join bars b on b.id = s.bar_id where l.drinker_id ="+str(target_drinker.id)+" and b.state='"+target_state+"'" ).fetchall()
        beer_tuples=connection.execute("select distinct l.drinker_id, b.id, b.name from likes l join beers b on l.beer_id = b.id where l.drinker_id ="+str(target_drinker.id)).fetchall()
        return render_template('results5.html', results1 = bar_tuples,results2 = beer_tuples)

    if request.method == 'POST' and media_select.validate_on_submit():
        print "media here"
        target_drinker = media_select.drinker.data
        target_media = media_select.media.data
        drinker_tuples=connection.execute("select d.* from friends f join drinkers d on f.friend_id = d.id where f.drinker_id="+str(target_drinker.id)+" and f.socialmedia_id='"+target_media+"'").fetchall()
        bar_tuples=connection.execute("select f.friend_id, b.* from friends f join frequents f1 on f1.drinker_id=f.friend_id join bars b on f1.bar_id=b.id where f.drinker_id="+str(target_drinker.id)+" and f.socialmedia_id='"+target_media+"'").fetchall()
        return render_template('results2.html', results1 = bar_tuples, results2 = drinker_tuples)

    if request.method == 'POST' and monthly_sale.validate_on_submit():
        print "monthly here"
        target_bar = monthly_sale.bar.data
        target_month = monthly_sale.month.data
        bar_tuples=connection.execute("select bar_id, beer_id, month, sum(qty) as sumq from sells where bar_id ="+str(target_bar.id)+" and month ="+target_month+" group by bar_id, beer_id, month").fetchall()
        beer_tuples=connection.execute("select distinct s.bar_id as bar_id, b1.name as bar_name, s.beer_id as beer_id, b.name as beer_name from bars b1 join sells s on s.bar_id=b1.id join beers b on b.id = s.beer_id where bar_id ="+str(target_bar.id)+" and month ="+target_month).fetchall()
        return render_template('results3.html', results1 = bar_tuples, results2 = beer_tuples)

    if request.method == 'POST' and daily_avgs.validate_on_submit():
        print "daily here"
        target_bar = daily_avgs.bar1.data
        target_month = daily_avgs.month1.data
        bar_tuples=connection.execute("select subq.bar_id, subq.beer_id, subq.month, avg(subq.sumq) as avgSoldPerDay from (select bar_id, beer_id, month, day, sum(qty) as sumq from sells where bar_id  ="+str(target_bar.id)+" and month ="+target_month+" group by bar_id, beer_id, month, day)subq group by month, beer_id, bar_id").fetchall()
        beer_tuples=connection.execute("select distinct s.bar_id as bar_id, b1.name as bar_name, s.beer_id as beer_id, b.name as beer_name from bars b1 join sells s on s.bar_id=b1.id join beers b on b.id = s.beer_id where bar_id ="+str(target_bar.id)+" and month ="+target_month).fetchall()
        return render_template('results4.html', results1 = bar_tuples, results2 = beer_tuples)

    return render_template('index.html', form1 = state_select, form2 = media_select, form3 = monthly_sale, form4 = daily_avgs, form5= user_likes)

if __name__ == '__main__':
    application.run(debug = True)
