def solution(x):
    num = list(str(x))
    total = 0
    for n in num:
        total += int(n)
    # print(total)
    if x%total==0:
        return True
    else: return False

x =11
print(solution(x))