def check(a, b, c): 
    total = a + b + c
    for i in range(2, total): 
        if total % i == 0 : return False 
    return True 

def solution(nums):
    answer = 0
    for i in range(0, len(nums) - 2): 
        for j in range(i+1, len(nums) - 1): 
            for k in range(j+1, len(nums)): 
                if check(nums[i], nums[j], nums[k]): answer += 1
    return answer 

#[1,2,3,4,5] => [a[i], a[i+1], a[i+2]]
"""
[1,2,3] [1,2,4] [1,2,5] [1,3,4] [1,3,5] [1,4,5] [2,3,4] [2,3,5] [2,4,5] [3,4,5]
"""

# from itertools import combinations 
# def check(a, b, c): 
#     total = a + b + c
#     for i in range(2, total): 
#         if total % i == 0 : return False 
#     return True 

# def solution(nums):
#     answer = 0
#     A = list(combinations(nums, 3))
#     for i in A: 
#         if check(i[0], i[1], i[2]): answer += 1
#     return answer