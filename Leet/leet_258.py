def addDigits(num):
    if num > 0:
        digit = list(str(num))
        total=0
        print(digit)
        count=0
        while 1:
            total=0
            for n in digit:
                total+=int(n)
            digit=[]
            digit = list(str(total))
            print(digit)
            if len(digit) == 1: break
        return int(digit[0])
    else: 
        return num
num=0
print(addDigits(num))