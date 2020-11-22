#fuel_left = int(input('How much gallons left ? \n'))
#mpg = int(input('How many miles do the car runs per 1 gallon ? \n'))
#distance_to_pump = int(input('How far is the nearest pump ? \n'))

#if distance_to_pump <=50 and fuel_left >=2 and mpg >=25:
    #print(True)
#else:
    #print(False)
    

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump <=50 and fuel_left >=2 and mpg >=25:
        return True
    else:
        return False
    