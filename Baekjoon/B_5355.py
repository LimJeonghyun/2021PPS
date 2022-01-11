num = int(input())
for i in range(num):
    nlist=(list(map(str, input().split())))
    n = float(nlist[0])
    for x in range(1,len(nlist)):
        if nlist[x] == "@": n = n*3
        elif nlist[x] == "%": n = n+5
        elif nlist[x] == "#": n = n-7
    print("%.2f"%n)
    nlist=[]

print(n)