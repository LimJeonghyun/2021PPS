max_index = 0
max_score = 0
for i in range(5):
    score = list(map(int, input().split()))
    if max_score < sum(score):
        max_score = sum(score)
        max_index = i

print(max_index + 1, max_score)

# list_c = []
# max = 0
# maxn = 0

# for i in range (5):
#     p = input("")
#     p = p.split()
#     total=0
#     for j in range (4):
#         total = total + int(p[j])
#     for j in range (len(list_c)):
#         if total > max:
#             max = total
#             maxn=i
#     list_c.append(total)


# if len(list_c) == 5:
#     print(maxn+1, max)