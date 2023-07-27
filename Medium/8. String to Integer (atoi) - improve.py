def myAtoi(s):
    """
    takes a string and converts it to a 32-bit signed integer, clamping it if it's out of range.
    
    Arguments:
    s (string)
    
    Returns:
    num (int32)
    """
    
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    num = '0'
    # Remove leading whitespace (and trailing)
    s = s.strip()

    if len(s) == 0:
        return 0
    # Sign of integer
    if s[0] == '+':
        sign = 'pos'
        s = s[1:]

    elif s[0] == '-':
        sign = 'neg'
        s = s[1:]
    else: 
        sign = 'pos'

    # Read digit characters up to first non-digit character
    count = 0
    while count < len(s) and s[count] in nums:
        num += s[count]
        count += 1 


    # convert to integer, add sign
    if sign == 'pos':
        num = int(num)
    
    elif sign == 'neg':
        num = -1*int(num)

    # Clamp integers outside of 32-bit signed range to 32-bit signed range
    if num < -2**(31):
        num = -2**(31)

    elif num > (2**31)-1:
        num = (2**31)-1

    return num    

# Bad performance, needs improvement - not sure how yet