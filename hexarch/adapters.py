from hexarch import app, db
from hexarch.services import OrderStorage


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    address = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)


class MemoryAdapter(OrderStorage):
    _db = db

    def add_order(self, data):
        self._db.session.add(data)
        self._db.session.commit()
