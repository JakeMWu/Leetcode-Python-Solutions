def IsPowerOfTwo(num):
    num_bin = f"{bin(num)[2:]}"
    char_count = {"1": 0,
                  }
    for num in num_bin:
        if num in char_count.keys():
            char_count[num] += 1
            
    if char_count["1"] == 1 and num_bin[-1] != 1:
        return True
        
    else:
        return False
