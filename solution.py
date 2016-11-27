import math

def binary(high, low, num, denom, negate, equal):
    """ Perform binary search to find quotient """
    mid = int(math.ceil((high+low)/2.0))
    if high == mid:
        if negate == -1:
            # if either num or denom is negative, go over
            return -high
        else:
            if equal == 1:
                # we want quotient to be 1 instead of 0
                return high
            return low
    # absolute difference between numerator and quotient*denominator
    temp = abs(num)-mid*abs(denom)
    if temp > 0:
        return binary(high, mid, num, denom, negate, equal)
    elif temp == 0:
        return negate*mid
    else:
        return binary(mid, low, num, denom, negate, equal)

def solution(num, denom):
    """ Return quotient and remainder given numerator and denominator in
    tuple form
    """
    if denom == 0:
        # denominator cannot be 0
        raise ArithmeticError("denominator cannot be zero!")
    if num == 0:
        #obvious case for numerator of 0
        return (0, 0)
    negate = 1
    equal = 0
    if num == denom:
        equal = 1
    if num*denom < 0:
        #used to decide whether to go over
        negate = -1
    quotient_space = abs(abs(num)-abs(denom))+1
    quotient = binary(quotient_space, 0, num, denom, negate, equal)
    remainder = num-quotient*denom
    return (quotient, remainder)
