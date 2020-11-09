# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# double_char("String") ==> "SSttrriinngg"

# double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"

# double_char("1234!_ ") ==> "11223344!!__  "

def double_char(s):
    word_double_chair = ""
    for i in s:
        word_double_chair += i*2
    return word_double_chair

print (double_char("String"))