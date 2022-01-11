def solution(n, times):
    pas = [0 for i in range(len(times))]
    times = list(sorted(times))
    if n%2 == 0: 
        pas[0]+=2
        n-=2
        for j in range(0,n,2):
            for i in range(len(times)):
                pas[i]+=1
    else:
        pas[0]+=1
        n-=1
        for j in range(0,n-1,2):
            for i in range(len(times)):
                pas[i]+=1

    print(pas)
        # n-=len(times)
        # if n == 0: break
        
    
    min = pas[len(times)-1]*times[len(times)-1]

    # for i in range(len(times)):
    #     if times[i]*pas[i] < min:
    #         min = times[i]*pas[i]
    return min

print(solution(6, [7,10]))