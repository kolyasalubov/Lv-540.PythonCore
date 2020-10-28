cap=int (input ( "Enter total number of seats in the bus:"))
on=int(input ( "Enter number of passengers on the bus: "))
wait=int(input ("Enter number of passengers waiting for the bus: "))
def enough(cap, on, wait):
    if wait - (cap - on) < 0:
        return False
    else:
        return wait - (cap - on)
print ( enough(cap, on, wait))