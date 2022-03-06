available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "HDMI cable",
                   "DVD drive"
                   ]
valid_choices = []
for i in range(1, len(available_parts) + 1): # adding 1 to len of range because the final value is not included
    valid_choices.append(str(i)) #using str because the customer is inputting strings: input will return a string- if their input is going to match this list then this list should also contain strings
print(valid_choices)
current_choice = "-"
computer_parts = [] #create an empty list

while current_choice != '0':
    if current_choice in valid_choices:
        print("Adding {}".format(current_choice))
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        computer_parts.append(chosen_part)
    else:
        print("Please add options from the list below:")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))

    current_choice = input()

print(computer_parts)


