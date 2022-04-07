def fizz_buzz(number: int) -> str:
    """
    Take an `int` and for every value between one and the provided `int`,
    return "fizz" for and value divisible by three, return "buzz" for
    any value divisible by five, and return "fizz buzz" for any value
    divisible by both three and five. Otherwise return the value.

    :param top: The int provided which is the top value.
    :return: "Fizz", "Buzz", "Fizz Buzz", or the value.
    """
    if (number % 3 == 0) and (number % 5 != 0):
        return "Fizz"
    elif (number % 5 == 0) and (number % 3 != 0):
        return "Buzz"
    elif (number % 3 == 0) and (number % 5 == 0):
        return "Fizz Buzz"
    else:
        return str(number)

input("Play Fizz Buzz.   Press ENTER to start")
print("Please type 'fizz' if number divisible by 3, 'buzz' if "
    "divisible by 5, and 'fizz buzz' if divisible by 3 and 5."
    "Or else print the value.")
value = "-"
for i in range(1, 101):
    if i % 2 == 0:
        if value == fizz_buzz(i):
            print("Correct!")
            continue
        else:
            print("Game over!")
            break
    else:
        print(fizz_buzz(i))
    value = input()
else:
    print("Congratulations, you won!")


