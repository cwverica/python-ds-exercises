def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """

    range_num = num
    factors = []
    if num % 2 != 0:
        range_num -= 1
    for val in range(1, int((range_num/2)+1)):
        if num % val == 0:
            factors.append(val)

    factors.append(num)
    return factors

