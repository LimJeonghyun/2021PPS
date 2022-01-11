num = int(input())
words = []
for i in range(num):
    word = input()
    words.append(word)

words = list(set(words))
words.sort()
words = list(sorted(words, key=len))

for i in range(len(words)):
    print(words[i])
