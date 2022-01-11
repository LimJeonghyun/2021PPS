def isPalindrome(s):
    s=list(s.lower())
    i = 0
    while i < len(s):
        if s[i].isalnum() == False:
            del s[i]
            i-=1
        i+=1
    sr = list(reversed(s))
    if s == sr: return True
    else : return False



s = "0P"
print(isPalindrome(s))