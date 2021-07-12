number = int(input(""))
name = []
for i in range (number):
    name.append(input(""))
player = []
for i in range (number):
    count = 0
    for j in range (number):
        if name[i][0] == name[j][0]:
            count+=1
        if count ==5 :
            player.append(name[i][0])
            break
player = sorted(list(set(player)))

if len(player) ==0:
    print("PREDAJA")
else:
    play = "".join(player)
    print(play)

