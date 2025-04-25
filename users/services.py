import stripe
from drf.settings import STRIPE_KEY
from rest_framework.reverse import reverse_lazy

stripe.api_key = STRIPE_KEY


def create_product(name):
    return stripe.Product.create(name=name)


def create_price(amount, product):
    return stripe.Price.create(
        currency="rub",
        unit_amount=int(amount * 100),
        product=product.get('id')
    )


def create_session(price):
    success_url = f"http://localhost:8000/{reverse_lazy('payments')}"
    session = stripe.checkout.Session.create(
        success_url=success_url,
        line_items=[{"price": price.get('id'), "quantity": 1}],
        mode="payment",
    )
    return session.get('id'), session.get('url')
