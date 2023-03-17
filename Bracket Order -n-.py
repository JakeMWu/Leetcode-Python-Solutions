def valid_parentheses(s):
    br_1 = 0 
    br_2 = 0
    br_3 = 0
    for char in s: 
        if char == "(" and br_1 >= 0:
            br_1 += 1
        elif char == ")" and br_1 > 0:
            br_1 -= 1
        elif char == "[" and br_2 >= 0:
            br_2 += 1
        elif char == "]" and br_2 > 0:
            br_2 -= 1
        elif char == "{" and br_3 >= 0:
            br_3 += 1
        elif char == "}" and br_3 > 0:
            br_3 -= 1
        else:
            return False
        
    return True
        
            
        