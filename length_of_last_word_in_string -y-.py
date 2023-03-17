def LastWord(s):
    if " " not in s.strip():
        return len(s.strip())
    else:
        count = 0 
        i = -1
        while s.strip()[i] != " ":
            i -= 1 
            count += 1
        return count
    
    
    
sentence_1 = "The quick brown fox jumped over the lazy dog"

sentence_2 = "a"

sentence_3 = "    oh    to  be      free      "