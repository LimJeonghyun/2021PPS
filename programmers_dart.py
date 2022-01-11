def solution(dartResult):
    dart = []
    temp=[]
    answer = 0
    for i in range(len(dartResult)):
        if dartResult[i].isdigit() and len(temp)!=0: 
            if dartResult[i-1].isdigit():
                temp.remove("1")
                temp.append("10")
            else:
                dart.append(temp)
                temp=[]
                temp.append(dartResult[i])
        elif i+1 == len(dartResult):
            temp.append(dartResult[i])
            dart.append(temp)
        else:temp.append(dartResult[i])
    print(dart)
    po = ["S", "D", "T"]
    op = ["*", "#"]
    ta = 0
    tl=[]
    for i in range(len(dart)):
        for j in range(len(dart[i])):
            for x in range(len(po)):
                if po[x] == dart[i][j]:
                    if x == 0: ta+=int(dart[i][j-1])
                    elif x == 1: ta+=int(dart[i][j-1])**2
                    elif x == 2: ta+=int(dart[i][j-1])**3
            for y in range(len(op)):
                if op[y] == dart[i][j]:
                    if y==0:
                        if len(tl)!=0:
                            tl[i-1]=tl[i-1]*2
                        ta=ta*2
                    else:ta=ta*(-1)
        tl.append(ta)
        ta=0
    for i in range(len(tl)):answer+=tl[i]
    return answer

dartResult="1D2S3T*"
print(solution(dartResult))