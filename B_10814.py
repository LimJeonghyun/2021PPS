num = int(input())
name = {}
for i in range(num):
    an = list(map(str, input().split()))
    name[an[1]] = an[0]
# sdidc=sorted(name.items(), reverse=True)
for a in sorted(name.items(), reverse=True):
    print(a[1], a[0])

# member_num = int(input())
# member_list = []

# for _ in range(member_num):
#     member_age, member_name = map(str, input().split())
#     member_age = int(member_age)
#     member_list.append((member_age, member_name))

# #나이 숫자 정렬 > 가입순 정렬
# member_list.sort(key = lambda member: (member[0]))

# for member in member_list:
#     print(member[0], member[1])