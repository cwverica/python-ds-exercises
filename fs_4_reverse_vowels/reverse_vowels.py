def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vow_ind = []
    str_list = list(s)
    for x in range(len(str_list)):
        if str_list[x] in 'aeiouAEIOU':
            vow_ind.append(x)

    for x in range(int(len(vow_ind)/2)):
        str_list[vow_ind[x]] = s[vow_ind[-(x+1)]]
        str_list[vow_ind[-(x+1)]] = s[vow_ind[x]]

    new_str = ''
    for char in str_list:
        new_str += char

    return new_str
