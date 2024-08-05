def add(*n) : 
    s = 0 
    for i in n :
        s += i  
    return s

def check(num):
    if num % 2  == 0 :
        return "Even"
    else:
        return "Odd"
    
def even(num):
    if num % 2 == 0 :
        return True 
    else:
        return False 
    
def odd(num):
    if num % 2 != 0 :
        return True 
    else:
        return False 
    
    
    