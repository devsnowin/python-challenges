# Give me the discount

"""
    Create a function in Python that accepts two parameters. 
    The first should be the full price of an item as an integer. 
    The second should be the discount percentage as an integer.
    The function should return the price of the item after the discount has been applied. 
    For example, if the price is 100 and the discount is 20, the function should return 80.
"""


def discount(price: int, discount_price: int) -> int:
    """
        Accepts price(int) and discount(int).
        Returns the price with discount
    """
    return price-discount_price


price = discount(100, 20)
print("The total price: ",price)
