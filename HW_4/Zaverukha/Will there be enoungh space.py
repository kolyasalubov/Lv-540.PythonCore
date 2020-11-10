def enough(cap, on, wait):
    if wait-(cap-on) < 0:
        return False
    else:
        return  wait-(cap-on)
        
    
    
  
