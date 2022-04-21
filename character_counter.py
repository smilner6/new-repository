# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}

# Text string
text = "Later in the course, you'll see how to use the collections Counter class."


for character in text.casefold():
    if character.isalnum():
        word_count[character] = word_count.setdefault(character, 0) + 1

print(word_count)
