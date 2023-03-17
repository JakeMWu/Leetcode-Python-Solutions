def longestCommonPrefix(strs):
    
    prefix = ""
    for i in range(len(min(strs, key=len))):
        for j in range(len(strs)):
            letter = strs[0][j]
            count = 0 
            if strs[j][i] == letter:
                continue
            else:
                count = 1
                break
        if count == 0:
            prefix + letter
            
        else: 
            break
    return prefix

strings = ["flower","flow","flight"]

print(longestCommonPrefix(strings))