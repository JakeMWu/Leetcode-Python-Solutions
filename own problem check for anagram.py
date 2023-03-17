def anagrams(string_1, string_2):
    dictionary_1 = {}
    dictionary_2 = {}
    for letter in string_1:
        letters = dictionary_1.keys()
        if letter in letters:
            dictionary_1[letter] += 1
        else:
            dictionary_1[letter] = 1

    for letter in string_2:
        letters = dictionary_2.keys()
        if letter in letters:
            dictionary_2[letter] += 1
        else:
            dictionary_2[letter] = 1
    if dictionary_1 == dictionary_2:
        return True
    else: 
        return False
    
print(anagrams("abcde", "dcba"))