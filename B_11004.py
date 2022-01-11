intp = list(map(int, input().split()))
num = input()
num=list(sorted(num))
num = ' '.join(num).split()
# num.remove(' ')
print(num[intp[1]-1])

# def _11004():
#     N, K = map(int, input().split(' '))
#     nums = list(map(int, input().split(' ')))

#     nums.sort()
#     print(nums[K-1])
# _11004()