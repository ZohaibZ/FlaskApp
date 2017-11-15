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

    def __init__(self, id, name, reviews, price, stars, occupancy, address, city, state, phone):
        self.id = id
        self.name = name
        self.reviews = reviews
        self.price = price
        self.stars = stars
        self.occupancy = occupancy
        self.type= type
        self.address = address
        self.city = city
        self.state = state
        self.phone = phone

    def __repr__(self):
        return "<Bar '{}'>".format(self.name)

class drinkers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    address = db.Column(db.String(128))
    city = db.Column(db.String(30))
    state = db.Column(db.String(30))
    reviews = db.Column(db.Integer)

    def __init__(self, id, name, reviews, price, stars, occupancy, address, city, state, phone):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.city = city
        self.state = state
        self.review = review

class brewery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    address = db.Column(db.String(128))
    city = db.Column(db.String(30))
    state = db.Column(db.String(30))
    country = db.column(db.String(30))
    phone = db.Column(db.String(30))
    beer = db.relationship('beers', backref='brewery', lazy ='dynamic')

    def __init__(self, id, name, address, city, state, country, phone):
        self.id = id
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.country = country
        self.phone = phone

class beers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brewery_id = db.Column(db.Integer, db.ForeignKey('brewery.id'))
    name = db.Column(db.String(30))

    def __init__(self, id, brewery_id, name):
        self.id = id
        self.brewery_id = brewery_id
        self.name = name
