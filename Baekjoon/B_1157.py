word = input("")
word = word.upper()

word_l = []
for w in word:
    word_l.append(w)

word_s = list(set(word_l))
max = 0

for w in word_s:
    count = 0
    for c in word_l:
        if w == c: count+=1
    if count > max:
        maxw = w
        max = count
    elif count == max:
        maxw = "?"  
print(maxw)