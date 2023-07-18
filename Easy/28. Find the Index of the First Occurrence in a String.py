def strStr(haystack, needle):
    """
    Given two strings, needle and haystack returns the index of the first occurance of needle in haystack or -1
    if needle isn't in haystack
    
    arguments:
    haystack (string)
    needle (string)
    
    Returns:
    index (integer) : index at which needle appears in haystack
    """
    index = -1 
    ln = len(needle)
    for i in range(len(haystack)):
        if haystack [i:i + ln] == needle:
            return i
        
    return index