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
