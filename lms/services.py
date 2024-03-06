
import stripe
from rest_framework.response import Response


def converter_for_price(pennies_price):
    """
    Converts value from pennies to rubles
    """
    rub_price = pennies_price * 100
    return rub_price


def get_create_product(product_title):
    """
    Creating product for payment service
    """
    product = stripe.Product.create(name=product_title)
    return product["name"]


def get_create_price(prod_name, amount):
    """
    Creating price for product
    """
    product_price = stripe.Price.create(
        currency="usd",
        unit_amount=amount,
        recurring={"interval": 'month'},
        product_data={"name": prod_name},
    )
    return product_price["id"]


def get_create_session(price_id):
    """
    Creating payment session
    returns: payment link
    """
    # Получите id цены из запроса
    payment_link = stripe.PaymentLink.create(
        line_items=[{"price": price_id, "quantity": 1}],
    )
    # Верните URL платежного линка
    return Response(f"payment link : {payment_link['url']} , payment id : {payment_link['id']}")