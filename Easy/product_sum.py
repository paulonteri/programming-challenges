# Product Sum

def productSum(array, multiplier=1):
    total = 0
    for i in array:
        if type(i) == list:
            total += productSum(i, multiplier + 1)
        else:
            total += i
    return total * multiplier
