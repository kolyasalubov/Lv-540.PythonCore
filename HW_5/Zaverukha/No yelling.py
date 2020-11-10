def filter_words(st):
    st = st.lower()
    st = st.capitalize()
    st = st.split()
    st = (" ".join(st))
    return st