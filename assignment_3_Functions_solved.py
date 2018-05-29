def absolute(num):
    if num < 0:
        return -num
    else:
        return num

def maximum(listy):
    a = listy[0]
    for number in listy:
        if number > a:
            a = number
        else:
            continue
    return a

