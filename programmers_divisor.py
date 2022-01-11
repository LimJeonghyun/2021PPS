def solution(left, right):
    answer = 0
    if 1<=left<=right<=1000:
        for i in range(left, right+1):
            count=0
            for j in range(1,i+1):
                if i%j == 0:
                    count+=1
            print(count)
            if count%2 == 1:
                i=-i
            answer+=i

    return answer

print(solution(24, 27))