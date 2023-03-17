def is_palindrome(x):
        xstr = str(x)
        Palindrome = True
        for i in range(len(xstr)//2):
            if xstr[i] == xstr[-i-1]:
                Palindrome = True
                continue
            else: 
                Palindrome = False 
                break 
        return(Palindrome)