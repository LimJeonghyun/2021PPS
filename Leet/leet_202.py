def isHappy(n):
    answer=list(str(n))
    total=0
    while 1:
        if int(n/10) == 0:
            if n==1 or n==7: return True
            else: return False
            break
        total = 0
        for i in range(len(answer)):
            total +=int(answer[i])**2
        n = total
        answer=list(str(total))
        # print(n)

n=7
print(isHappy(n))