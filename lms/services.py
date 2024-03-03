import stripe
from rest_framework import status
from rest_framework.response import Response


def converter_for_price(pennies_price):
    """
    Converts value from pennies to rubles
    """
    rub_price = pennies_price * 100
    return rub_price


def get_create_product(product_title, stripe_api_key):
    """
    Creating product for payment service
    """
    stripe.api_key = stripe_api_key
    stripe.Product.create(name=product_title)
    return Response({"message": "Success!"}, status=status.HTTP_200_OK)


def get_create_price(stripe_api_key, currency, unit_amount, interval, product_title):
    """
    Creating price for product
    """
    stripe.api_key = stripe_api_key
    stripe.Price.create(
        currency=currency,
        unit_amount=unit_amount,
        recurring={"interval": interval},
        product_data={"name": product_title},
    )
    return Response({"message": "Success!"}, status=status.HTTP_200_OK)


def get_create_session(stripe_api_key, price_id, quantity=1):
    """
    Creating payment session
    returns: payment link
    """
    stripe.api_key = stripe_api_key
    price_id = price_id
    # Получите id цены из запроса
    payment_link = stripe.PaymentLink.create(
        line_items=[{"price": price_id, "quantity": quantity}],
    )
    # Верните URL платежного линка
    return Response(payment_link['url'])
