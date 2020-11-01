cap=int(input("Enter the number of passangers"))
on=int(input("Enter the number of passangers on the bus"))
wait=int(input("Enter the number of passangers  waiting to get on to the bus"))

def enough():
    if  cap-on>=0 and wait - (cap-on)>=0:
         print("Only the first", cap-on, "passangers can take places" )
    elif wait <= (cap-on):     
        print("All left passangers can take place")
enough() 