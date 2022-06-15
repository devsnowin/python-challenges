# Count the vowels in a string

"""
    Create a function in Python that accepts 
    a single word and returns the number of vowels in that word. 
    In this function, only a, e, i, o, and u will be counted as vowels — not y.
"""


def count_vowels(word:str) -> str:
    """
        Accepts a string (word).
        Returns the vowels in a word
    """

    numbers = ['1','2','3','4','5','6','7','8','9','0']
    vowels = ['a', 'e', 'i', '0', 'u']
    for letter in word:
        if letter not in numbers:
            if letter in vowels:
                return letter
    print("Please enter a string value!")

vowels = count_vowels(input("Enter a single word: "))
print("The vowel values are: ", vowels)
