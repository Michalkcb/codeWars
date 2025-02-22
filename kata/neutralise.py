def neutralise(s1, s2):
    result = ""                 
    for a, b in zip(s1, s2):  
        if a == b:              
            result += a      
        else:              
            result += '0'
    return result   
