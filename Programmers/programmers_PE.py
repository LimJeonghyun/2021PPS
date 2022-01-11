def solution(n, lost, reserve):
    # a_sub_b = [x for x in a if x not in b]
    holes = set(lost) - set(reserve)
    spares = set(reserve) - set(lost)
    # print(holes, spares)
    answer=n-len(holes)
    for each in holes:
        if each-1 in spares:
            answer+=1
            spares.remove(each-1)
        elif each+1 in spares:
            answer+=1
            spares.remove(each+1)
    return answer

print(solution(7, [1,3,5], [3,4,7]))
#return 4