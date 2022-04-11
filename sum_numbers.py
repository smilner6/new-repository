def sum_numbers(*numbers: tuple)-> float:
    """
    Unpack a tuple of passed values and return their sum.
    :param numbers: The values to be added.
    :return: The result of the sum of all passed values.
    """
    result = sum(numbers)
    return result


print(sum_numbers(1.1, 2.2, 5.5))

