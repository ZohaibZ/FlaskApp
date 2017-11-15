from flask import Flask, render_template, request, redirect, url_for
from application import db
from application.models import drinkers, bars
from application.forms import stateSelection

application = Flask(__name__)
application.secret_key = 'my336DbProject'

@application.route('/', methods=['GET', 'POST'])
@application.route('/index', methods=['GET', 'POST'])
def index():
    state_selection = stateSelection(request.form)

    # if request.method == 'POST' and form1.validate():
    #     data_entered = Data(notes=form1.dbNotes.data)
    #     try:
    #         db.session.add(data_entered)
    #         db.session.commit()
    #         db.session.close()
    #     except:
    #         db.session.rollback()
    #     return render_template('thanks.html', notes=form1.dbNotes.data)

    if request.method == 'POST' and state_selection.validate():
        target_state = state_selection.state.data
        bar_tuples = bars.query.filter_by(state=target_state)
        for bar in bar_tuples:
            print(bar.name)
        db.session.close()
        return render_template('results.html', results = bar_tuples)
    return render_template('index.html', form = state_selection)

if __name__ == '__main__':
    application.run(debug = True)
