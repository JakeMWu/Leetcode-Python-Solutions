def isAnagram(s, t):
    if len(s) != len(t): 
        return False
    
    s1 = {}
    s2 = {}
    
    for letter in s:
        if letter in s1.keys():
            s1[letter] += 1 
        else: 
            s1[letter] = 1 
            
    for letter in t:
        if letter in s2.keys():
            s2[letter] += 1 
        else: 
            s2[letter] = 1 
            
    if s1 == s2:
        return True
    
    else: 
        return False

# Above is a slow solution, below is much faster possible due to 
# speed of operating with sets, speed of the .count method and 
# not needing to perform memory operations w/ the dictionaries

def isAnagram2(s, t):
    if len(s) != len(t):
        return False
    
    for letter in set(s):
        if s.count(letter) != t.count(letter):
            return False
    
    return True


    