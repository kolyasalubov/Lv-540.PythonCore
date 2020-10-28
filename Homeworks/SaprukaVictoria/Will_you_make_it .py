distance_to_pump=int (input ("Enter distance: "))
mpg=int (input ("Enter miles per gallon for your car: "))
fuel_left=int (input ("Enter how much fuel left: "))
def zero_fuel(distance_to_pump, mpg, fuel_left):
    res = mpg * fuel_left

    if distance_to_pump <= res:
        return True
    else:
        return False
print (zero_fuel(distance_to_pump, mpg, fuel_left))

