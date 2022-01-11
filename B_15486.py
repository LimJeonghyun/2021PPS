import sys

N = int(input())

day = N
Con, Pr = [], []
mp = [0 for x in range(N+1)]

for i in range(N):
    temp = list(map(int, input().split()))
    Con.append(temp[0])
    Pr.append(temp[1])

for i in range(0, N):
    if Con[i] <= N - i:
        mp[i+Con[i]] = max(mp[i+Con[i]], mp[i]+Pr[i])
    mp[i+1] = max(mp[i+1], mp[i])

print(mp[N])





# 
        
#     