def enough(cap, on, wait):
    if cap > wait and wait == on and cap == on+wait :
        return 0
    elif cap > on  and on > wait and cap > wait:
        return on-wait
    elif cap > wait and wait == on and cap > wait + on :
        return 0
    