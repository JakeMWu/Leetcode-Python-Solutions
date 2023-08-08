def isAnagram(str1, str2):
    if len(str1) != len(str2):
        return False
    for letter in set(str1):
        if str1.count(letter) == str2.count(letter):
            continue
        else:
             return False
    return True 

def groupAnagrams(self, strs):
    """
    Takes an array of strings and sorts them together based on 
    whether they are anagrams. 
    """
    grouped = [[strs[0]]]
    for item in strs[1:]:
        added = False
        for group in grouped:
            if isAnagram(item,group[0]):
                group.append(item)
                added = True
                break
        if added == False:
            grouped.append([item])
    return grouped

# Very slow but 100% memory efficient