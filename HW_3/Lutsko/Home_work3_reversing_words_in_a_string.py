def reverse(st):
# reversing-words-in-a-string
    words = st.split()
    words = list(reversed(words))
    reversed_string = " ".join(words)
    return reversed_string