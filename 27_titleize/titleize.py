def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    word_list = phrase.lower().split()
    return_string = ''
    for word in word_list:
        return_string += word[0].upper() + word[1:] + ' '
    return return_string[:-1]
