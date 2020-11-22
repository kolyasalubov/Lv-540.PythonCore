def double_char(s):
    s = list(s)
    new_list = []
    for x in s:
        new_list.append(x*2)
    return ''.join(new_list)