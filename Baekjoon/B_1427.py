num = input()
num = list(num)
num = list(sorted(num, reverse=True))
print(''.join(num))