menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

gross_meat = "spam"

# remove spam then print list

for meal in menu:
    if gross_meat in meal:
        top_index = len(meal)-1
        for index, value in enumerate(reversed(meal)):
            if value == gross_meat:
                del meal[top_index - index]
        print(meal)
    else:
        print(meal)

# print items as long as not spam

for meal in menu:
    for item in meal:
        if item == gross_meat:
            continue
        else:
            print(item)



