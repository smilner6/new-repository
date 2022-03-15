#magical adder- my solution which worked yay!

print("""Please enter 3 numbers to compute, separated by commas""")
numbers = input()
int_values = list("".join(numbers))
for index in range(len(int_values)-1, -1, -1):
    if int_values[index] == ",":
        del int_values[index]
for index in range(len(int_values)):
    int_values[index] = int(int_values[index])
answer = int_values[0] + int_values[1] - int_values[2]
print(answer)

#python tutorital solution
# Take input from the user
user_input = input("Please enter three numbers: ")

# Split the given input string into 3 parts
string_tokens = user_input.split(",")

# Convert the tokens into integers
int_tokens = []
for st in string_tokens:
    int_tokens.append(int(st))

# Calculate the result: a + b - c
a, b, c = int_tokens
result = a + b - c
# result = int_tokens[0] + int_tokens[1] - int_tokens[2]

# Output the result
