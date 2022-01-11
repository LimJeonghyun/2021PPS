def checkRecord(s):
    case = 0
    if s.count("A") >= 2: return False
    else:
        a=0
        case = 2
        while 1:
            a=s.find("L", s.find("L", a))
            if a>=0 and a+2<len(s):
                if s[a] == s[a+1] == s[a+2]:
                    case = 1
                    break
            if a == -1 or a == len(s)-1: break
            a+=1
            
        if case == 1: return False
        else: return True

    
s="PLLPLLLLPP"
print(checkRecord(s))
