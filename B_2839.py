sugar = int(input())

bag = 0
while sugar >= 0 :
    if sugar % 5 == 0 :  # 5의 배수이면
        bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    sugar -= 3  
    bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else :
    print(-1)


# num = int(input())
# count = 0
# countlist = []

# if num%5 == 0 or num%3 == 0:
#         if num%5 ==0 : countlist.append(num/5)
#         elif num%3 ==0 : countlist.append(num/3)
        
# while 1:
#     if num == 0: break
#     if num-5 < 0 and num-3 < 0:
#         count = -1
#         break
#     elif num-5 > 0:
#         num-=5
#         count+=1
#     elif num - 3 > 0:
#         num-=3
#         count+=1
#     if num%5==0:
#         count = count+num/5
#         num = num%5
#     if num%3==0:
#         count = count+num/3
#         num = num%3
# countlist.append(count) 
# countlist=list(sorted(countlist))
# # print(countlist)
# if len(countlist) !=1 and countlist[0] ==-1:
#     print(int(countlist[1]))
# else: print(int(countlist[0]))

#18  4
# 4 -1
# 6 2
# 9 3
# 11 3