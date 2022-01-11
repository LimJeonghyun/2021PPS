def dailyTemperatures(temperatures):
    answer = [0 for i in range(len(temperatures))]
    print(answer)
    
    for i in range(len(temperatures)):
        for j in range(i+1, len(temperatures)):
            answer[i]+=1
            if temperatures[i] < temperatures[j]:
                break
            elif temperatures[i] >= temperatures[j] and j == len(temperatures)-1: answer[i]=0
            
    return answer

temperatures =  [34,80,80,80,34,80,80,80,34,34]
print(dailyTemperatures(temperatures))
# Output: [1,1,4,2,1,1,0,0]