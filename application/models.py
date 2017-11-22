from application import db

class bars(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    reviews = db.Column(db.Integer)
    price = db.Column(db.Integer)
    stars = db.Column(db.Float)
    occupancy = db.Column(db.Integer)
    type = db.Column(db.String(30))
    address = db.Column(db.String(128))
    city = db.Column(db.String(30))
    state = db.Column(db.String(30))
    phone = db.Column(db.String(30))

    def __repr__(self):
        return "{}".format(self.name)

class drinkers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    address = db.Column(db.String(128))
    city = db.Column(db.String(30))
    state = db.Column(db.String(30))
    reviews = db.Column(db.Integer)

    def __repr__(self):
        return "{}".format(self.name)

class brewery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    address = db.Column(db.String(128))
    city = db.Column(db.String(30))
    state = db.Column(db.String(30))
    country = db.column(db.String(30))
    phone = db.Column(db.String(30))


class beers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brewery_id = db.Column(db.Integer, db.ForeignKey('brewery.id'))
    name = db.Column(db.String(30))


class bartenders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))

class bartends(db.Model):
    bartender_id = db.Column(db.Integer, db.ForeignKey('bartenders.id'), primary_key=True)
    bar_id = db.Column(db.Integer, db.ForeignKey('bars.id'), primary_key=True)
    month = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Integer, primary_key=True)
    shift = db.Column(db.Integer, primary_key=True)
    tips = db.Column(db.Integer)

class frequents(db.Model):
    drinker_id = db.Column(db.Integer, db.ForeignKey('drinkers.id'), primary_key=True)
    bar_id = db.Column(db.Integer, db.ForeignKey('bars.id'), primary_key=True)

class occupations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

class sells(db.Model):
    bar_id = db.Column(db.Integer, db.ForeignKey('bars.id'), primary_key=True)
    beer_id = db.Column(db.Integer, db.ForeignKey('beers.id'), primary_key=True)
    month = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

class socialmedia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

class works(db.Model):
    drinker_id = db.Column(db.Integer, db.ForeignKey('drinkers.id'), primary_key=True)
    occupation_id = db.Column(db.Integer, db.ForeignKey('occupations.id'), primary_key=True)
    salary = db.Column(db.Integer)

class friends(db.Model):
    drinker_id = db.Column(db.Integer, db.ForeignKey('drinkers.id'), primary_key=True)
    friend_id = db.Column(db.Integer, db.ForeignKey('drinkers.id'), primary_key=True)
    socialmedia_id = db.Column(db.Integer, db.ForeignKey('socialmedia.id'), primary_key=True)

class pays(db.Model):
    bar_id = db.Column(db.Integer, db.ForeignKey('bars.id'), primary_key=True)
    beer_id = db.Column(db.Integer, db.ForeignKey('beers.id'), primary_key=True)
    month = db.Column(db.Integer, primary_key=True)
    qty = db.Column(db.Integer)
    price = db.Column(db.Float)

class visits(db.Model):
    drinker_id = db.Column(db.Integer, db.ForeignKey('drinkers.id'), primary_key=True)
    bar_id = db.Column(db.Integer, db.ForeignKey('bars.id'), primary_key=True)
    month = db.Column(db.Integer, primary_key=True)
    qty = db.Column(db.Integer,primary_key=True)

class likes(db.Model):
    drinker_id = db.Column(db.Integer, db.ForeignKey('drinkers.id'), primary_key=True)
    beer_id = db.Column(db.Integer, db.ForeignKey('beers.id'), primary_key=True)
