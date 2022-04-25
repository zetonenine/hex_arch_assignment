from flask_wtf import FlaskForm
from wtforms import StringField
from hexarch import app
from hexarch.adapters import Order, MemoryAdapter
from hexarch.services import CreateOrderCase


class OrderForm(FlaskForm):
    name = StringField('name')
    address = StringField('address')


def create_order_case() -> CreateOrderCase:
    return CreateOrderCase(MemoryAdapter())


@app.route("/create", methods=['POST'])
def create_order():
    form = OrderForm()
    if form.validate():
        order = Order()
        form.populate_obj(order)
        create_order_case().create_order(order)
        return "<h1>Success</h1>"
    else:
        return "<h1>Failed</h1>"
