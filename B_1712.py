enter = list(map(int, input().split()))
A,B,C = enter[0], enter[1], enter[2]
if (C - B) <= 0:
    print("-1")
else:
    N = A / (C - B)
    N = N + 1
    print(int(N))

