# Find three largest numbers in array

def findThreeLargestNumbersOne(array):
    one = None
    two = None
    three = None
    for i in array:
        if one == None or i > one:
            three = two
            two = one
            one = i
        elif two == None or i > two:
            three = two
            two = i
        elif three == None or i > three:
            three = i
    return [three, two, one]
