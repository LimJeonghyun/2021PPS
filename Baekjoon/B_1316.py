number = int(input(""))
word = []
for i in range (number):
    word.append(input(""))

index = -1
result = 0

for ch in word:
    answer = 0
    chs = list(set(ch))
    for i in range (len(chs)):
        tem  = []
        while 1:
            index = ch.find(chs[i], index+1)
            if index == -1:
                break
            tem.append(index)
        if len(tem) == 1:
            answer+=1
        else:
            count = 0
            for i in range(len(tem)-1):
                if tem[i]+1 == tem[i+1]:
                    count+=1
                else: break
            if count == len(tem)-1: answer+=1
    if answer == len(chs) : result+=1

print(result)
