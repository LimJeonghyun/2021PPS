# M 층 / N 층별 창문수
M, N = [int(x) for x in input().split()]

type_counts = [0 for i in range(5)]
# print(types)
windows = list()
# temp = input().split("#")
# print(temp)
rlt = list()


for m in range(M):
    start = input()
    types = [0 for _ in range(N)]
    for i in range(4):
        windows = input().split("#")[1:-1]
        for idx, w in enumerate(windows):
            if w == "****":
                types[idx] += 1
    #print(types)
    rlt.append(types)
end = input()
# print(rlt)

for r in rlt:
    type_counts[0] += r.count(0)
    type_counts[1] += r.count(1)
    type_counts[2] += r.count(2)
    type_counts[3] += r.count(3)
    type_counts[4] += r.count(4)

# print(type_counts)
check = ' '.join([str(x) for x in type_counts])
print(check)

# M, N = map(int, input().split())

# window = []

# while len(window) != 5*M+1:
#     window.append(input())

# row, col = [], []
# for m in range (M):
#     row.append(5*M+1)
# result = []
# for r in row:
#     for c in col:
#         tmp = []
#         tmp.append(window[r][c:c+4])
#         tmp.append(window[r+1][c:c+4])
#         tmp.append(window[r+2][c:c+4])
#         tmp.append(window[r+3][c:c+4])
#         result.append(tmp)
# print(result)
# print(result.count(0), result.count(1), result.count(2), result.count(3), result.count(4))

