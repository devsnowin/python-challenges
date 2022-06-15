# Are the Xs equal to the Os?

"""
    Create a Python function that accepts a string. 
    This function should count the number of Xs and the number of Os in the string. 
    It should then return a boolean value of either True or False.
    If the count of Xs and Os are equal, then the function should return True. 
    If the count isn't the same, it should return False. 
    If there are no Xs or Os in the string, it should also return True because 0 equals 0. 
    The string can contain any type and number of characters.
"""


def count(value:  str) -> bool:
    """
        Accepts the string value.
        Returns the boolean value depends upon the condition given.
    """

    x = 0
    o = 0

    for letter in value:
        if letter == 'x' or letter == 'X':
            x+=1
        elif letter == 'o' or letter == 'O':
            o+=1

    if x != o:
        return False
    else:
        return True


founded_result = count("zooxx")
print(founded_result)
