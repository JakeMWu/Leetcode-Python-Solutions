def LengthOfLongestSubString(s):
    long_string = ''
    temp_string = ''
    
    for i in range(len(s)):
        temp_string = s[i]
        for j in range(i+1, len(s)):
            if s[j] not in temp_string:
                temp_string += s[j]
            else:
                break
        if len(temp_string) > len(long_string):
            long_string = temp_string
            
        return len(long_string)





def LengthOfLongestSubString1(s):
    long = 1
    
    for i in range(len(s)):
        short = 1
        temp_dic = {}
        temp_dic[s[i]] = 0
        
        for j in range(i+1, len(s)):
            if s[j] not in temp_dic.keys():
                temp_dic[s[j]] = 0
                short += 1
            else: 
                break
            
            if short > long:
                long = short
                
    return long
                
# Both above solutions have O(n^2) time complexity because of the nested loops and are therefore slow. They are also essentially the same with
# slight differences in implementation

def lengthOfLongestSubstring2(s):
    if len(s) == 0:
        return 0

    max_length = 0           # Variable to store the maximum length of the substring without repeating characters.
    start_index = 0          # Variable to keep track of the start index of the current substring being considered.
    char_index_map = {}      # Map to store the last index of each character seen in the string.

    for i in range(len(s)):
        if s[i] in char_index_map and char_index_map[s[i]] >= start_index:
            # If the character has been seen before and its index is greater than or equal to the current start_index,
            # update the start_index to the next index of the repeating character to start a new substring without repeating characters.
            start_index = char_index_map[s[i]] + 1

        char_index_map[s[i]] = i  # Update the index of the character in the char_index_map.

        current_length = i - start_index + 1  # Calculate the current length of the substring.

        max_length = max(max_length, current_length)  # Update the max_length to the maximum between the current length and the previous maximum length.

    return max_length  # Return the max_length, which represents the length of the longest substring without repeating characters.