password = []
vowel = ['a','e','i','o','u']
while 1:
    psw = input("")
    if psw =="end":break
    password.append(psw)
case = 0
for word in password:
    # print(word)
    for i in range(len(word)):
        if word[i] in vowel:
            # print("yes")
            case = 1
            break
        else: case = 2
    # if case == 2:
    #     print("%s is not acceptable."%word)
    if case ==1:
        countv=0
        countc=0
        for i in range(len(word)):
            if word[i] in vowel:
                countv+=1
                countc=0
            elif not word[i] in vowel:
                countc+=1
                countv=0
            if countc >= 3 or countv >= 3:
                case = 2
                break
        # if case == 2:
        #     print("%s is not acceptable."%word)
        if case == 1:
            for i in range(len(word)-1):
                if word[i] == word[i+1]:
                    if word[i] != 'o' and word[i+1] != 'o':
                        if word[i] != 'e' and word[i+1] != 'e':
                            case = 2
                            break
    if case == 2: print("<%s> is not acceptable."%word)
    elif case == 1: print("<%s> is acceptable."%word)
               

# print(password)
    