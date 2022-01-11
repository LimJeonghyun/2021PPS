def solution(N, stages):
    num=len(stages)
    answer = []
    final = {}
    for i in range(1,N+1):
        fail = stages.count(i)
        if num ==0:
            final[i]=0
        else: final[i] = fail/num
        num = num-fail
    answer = [stage[0] for stage in sorted(final.items(), reverse=True, key=lambda x: (x[1]))]
    return answer

stages = [2,3,1,4,6]
print(solution(5, stages))
# result = [3,4,2,1,5]
# answer? final? 무슨 차이??