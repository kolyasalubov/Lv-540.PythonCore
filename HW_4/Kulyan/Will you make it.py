def zero_fuel(distance_to_pump, mpg, fuel_left):
    a = mpg * fuel_left

    if distance_to_pump <= a:
        return True
    else:
        return False
    