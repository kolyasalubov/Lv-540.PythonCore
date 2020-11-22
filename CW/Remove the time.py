def shorten_to_date(long_date):
    new_list = long_date.split(',')
    new_list.pop()
    return ' '.join(new_list)