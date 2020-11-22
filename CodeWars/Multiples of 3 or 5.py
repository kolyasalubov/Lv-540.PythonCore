def solution(number):
    
    suma=0
    
    for value in range(number):
        
        if value % 3 == 0:
            suma += value
            
        if value % 5 == 0:
            suma += value
            
    if number < 0:
        return 0
    return suma