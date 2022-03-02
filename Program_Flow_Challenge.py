
options = """Please pick a snack for lunch tomorrow:
1. Triscuits
2. Goldfish
3. Cheese and Crackers
4. Peanuts 
0. Exit """

#
# print(options)
#
# while True:
#     choice = input()
#     if choice in "1234":
#         print("Option {} is a great choice! What will you have/"
#             "tomorrow?".format(choice))
#     elif choice == "0":
#         print("no snack for you")
#         break
#     else:
#         print(options)

choice = "-"
while choice != "0":
    if choice in"1234":
        print("You chose {}".format(choice))
    else:
        print(options)
    choice = input()


