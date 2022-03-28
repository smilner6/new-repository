def multiply(x, y):
    """
    Get two `int` values for the input. Multiply the values.

    The function will only accept valid integers.

    :param x: The first `int` value.
    :param y: The second `int` value.
    :return: The product of the two `int` values.
    """
    result = x * y
    return result


def is_palindrome(string):
    """
    Get a string value from the input. Evaluate for equality
    when reversed.

    :param string: The `str` that the user inputs.
    :return: A `bool` value reflecting the outcome of the
    evaluation.
    """
    # backwards = string[::-1]
    # return backwards == string
    return string.casefold()[::-1] == string.casefold()


def palindrome_sentence(sentence):
    """
    Get a String from the user input. Iterate through the `str`
    to evaluate for alphanumeric characters. Build a `str` of
    only the alphanumeric characters in the input String. Call
    the is_palindome function to evaluate for a palindrome.
    :param sentence: The `str` that the user inputs.
    :return: The `bool` result of the is_palindrome function
    once called.
    """
    string = ""
    for item in sentence:
        if item.isalnum():
            string += item
    return is_palindrome(string)

help(multiply)
help(is_palindrome)
help(palindrome_sentence)

# sentence = input("Please enter a sentence to check: ")
# if palindrome_sentence(sentence):
#     print("{} is a palindrome".format(sentence))
# else:
#     print("{} is not a palindrome".format(sentence))

#
# print()
#
# word = input("Please enter a word or sentence to check: ")
# if palindrome_sentence(word):
#     print("{} is a palindrome".format(word))
# else:
#     print("{} is not a palindrome".format(word))

answer = multiply(18, 3)
print(answer)
