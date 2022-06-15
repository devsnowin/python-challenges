# Hide the credit card number

"""
    Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "4444444444444444", then it should return "4444".
"""


def hide_numbers(card_number:str) -> str:
    """
        Accepts a string value or number.
        Hide the last four digital of the string given
    """
    
    stars = "*" * (len(card_number) - 4);
    return f"{stars}{card_number[-4:]}"

secret_number = hide_numbers("4444444444444444")
print("The pin number is: ", secret_number)
