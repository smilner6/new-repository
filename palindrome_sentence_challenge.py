def palindrome_sentence(string):
    pal_query = ""
    for item in string.casefold():
        if item.isalnum():
            pal_query += item
        else:
            del item
    if pal_query[::-1] == pal_query:
        return(True)
    else:
        return(False)

sentence = input("Please enter a sentence to check: ")
if palindrome_sentence(sentence):
    print("'{}' is a palindrome".format(sentence))
else:
    print("{} is not a palindrome".format(sentence))