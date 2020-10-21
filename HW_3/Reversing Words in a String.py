# You need to write a function that reverses the words in a given string. A word can also fit an empty string. If this is not clear enough, here are some examples:

# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

# reverse('Hello World') == 'World Hello'
# reverse('Hi There.') == 'There. Hi'


def reverse(phrase):
    words = phrase.split(" ")
    reversedword = ""
    for word in reversed(words):
        if word != "":
            reversedword += word
            reversedword +=  " "
    return reversedword.strip ()

print (reverse(" Hello how are you?"))