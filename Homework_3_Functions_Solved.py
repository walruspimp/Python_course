#Average of a list

def average(listeroo):
    a = 0
    if len(listeroo) == 0:
        return 0
    for number in listeroo:
        a = a + number
    return a/len(listeroo)



#Median of a List

def median(listeroo):
    if len(listeroo) == 0:
        return 0
    elif len(listeroo)%2 == 0:
        return (listeroo[(len(listeroo)//2)] + listeroo[((len(listeroo)//2)-1)])/2  
    else:
        return listeroo[(len(listeroo)//2)]

