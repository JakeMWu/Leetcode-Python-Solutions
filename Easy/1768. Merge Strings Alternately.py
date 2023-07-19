def mergeAlternately(word1, word2):
    """
    Takes two strings, word1 and word2 and merges them in alternating order.

    Arguments:
    word1 (string)
    word2 (string)

    Returns:
    new_word (string): string of word1 and word2 alternating
    """
    new_word = ''
    if len(word1) <= len(word2):
        for i in range(len(word1)):
            new_word += word1[i]
            new_word += word2[i]
        new_word += word2[len(word1):]
    
    elif len(word2) <= len(word1):
        for i in range(len(word2)):
            new_word += word2[i]
            new_word += word1[i]
        new_word += word1[len(word2):]
        
    return new_word