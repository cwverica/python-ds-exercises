def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    if parens.count('(') != parens.count(')'):
        return False
    opened = 0
    for paren in parens:
        if paren == ')':
            opened -= 1
            if opened < 0:
                return False
        if paren == '(':
            opened += 1
    if opened != 0:
        return False
    return True
