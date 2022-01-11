# ascii로 바꾸어 계산
def ibm (words):
    word=""
    for ch in words:
        if ch == "Z": word+="A"
        else: word += chr(ord(ch)+1)
    return word

num = int(input())
lists = []
for i in range (num):
    lists.append(ibm(input()))

for i in range (len(lists)):
    print("String #%d"%(i+1))
    print(lists[i])
    if i+1 != len(lists): print()
