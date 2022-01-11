number = int(input(""))

answer = []
for i in range (number):
    answer.append(list(input("")))

for i in range (len(answer)):
    score = 0
    pre = []
    # print(answer[i])
    for j in range (len(answer[i])):
        if answer[i][j] == 'O':
            score = 1
            if j > 0 and pre[j-1] >= 1:
                score = pre[j-1]+1
            pre.append(score)
        else:
            score = 0
            pre.append(score)
    total = 0
    for j in range (len(pre)):
        total = total+pre[j]

    print(total)