from math import log10, floor
from random import shuffle

def roundsf(number, sf):
    if number == 0:
        return 0
    try:
        return round(number, sf-1-int(floor(log10(abs(number)))))
    except:
        return number

def rand_partition(data, fraction):
    ldata = list(data)
    shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]