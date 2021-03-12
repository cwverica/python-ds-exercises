def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = ['a', 'e', 'i', 'o', 'u']

    vowel_count = dict()
    for letter in phrase.lower():
        if letter in vowels:
            if letter in vowel_count.keys():
                vowel_count[letter] += 1
            else:
                vowel_count[letter] = 1
    return vowel_count