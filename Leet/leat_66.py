def plusOne(digits):
        cal = 0
        l = len(digits)-1
        for i in range (len(digits)):
            cal=cal+digits[i]*(10**l)
            l-=1
        cal=cal+1
        
        new = list(str(cal))
        return new

print(plusOne([8,9,9]))