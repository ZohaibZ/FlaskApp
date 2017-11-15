from application import db
from application.models import bars, drinkers

db.create_all()
print "Db created"
