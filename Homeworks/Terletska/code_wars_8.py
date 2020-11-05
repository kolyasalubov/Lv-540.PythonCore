def correct_tail(body, tail):
    if body[len(body) - 1] == tail:
        return True
    return False
print(correct_tail(input(),input()))
