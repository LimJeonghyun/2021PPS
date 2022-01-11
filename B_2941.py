croatian = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = "c=c="
count=0
for i in range(len(croatian)):
    a=0
    while word.find(croatian[i]) != -1:
        a=word.find(croatian[i],word.find(croatian[i], a))
        print(a)
        count+=1
print(count)