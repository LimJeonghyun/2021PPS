rest = []
for i in range(10):
    N = int(input(""))
    rest.append(N%42)
rest = list(set(rest))
print(len(rest))
print(rest)