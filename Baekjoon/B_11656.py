s=  input()
sl = []
for i in range(len(s)):
    sl.append(s[i:])
sl = list(sorted(sl))
for ch in sl:
    print(ch)