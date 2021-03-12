def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    set1 = set(str(num1))
    set2 = set(str(num2))

    # if len(set1) != len(set2):
    #     return False
    # if len((set1 & set2)) != len(set1) or len((set1 & set2)) != len(set2):
    #     return False
    for val in set1:
        if str(num1).count(val) != str(num2).count(val):
            return False
    for val in set2:
        if str(num1).count(val) != str(num2).count(val):
            return False
    return True
