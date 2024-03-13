
import stripe


def converter_for_price(pennies_price):
    """
    Converts value from pennies to rubles
    """
    rub_price = pennies_price * 100
    return rub_price


def create_product(product_title):
    """
    Creating product for payment service
    """
    product = stripe.Product.create(name=product_title)
    return product["name"]


def create_price(prod_name, amount):
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


def create_session(price_id):
    """
    Creating payment session
    returns: payment link
    """
    session = stripe.PaymentLink.create(
        line_items=[
            {
                'price': price_id,
                'quantity': 1,
            },
        ],
    )
    return session["url"]
