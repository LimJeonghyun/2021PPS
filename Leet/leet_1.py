def twoSum(nums, target):
    answer = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            # print(nums[i]+nums[j])
            if nums[i]+nums[j] == target:
                answer.append(i)
                answer.append(j)
                break

    return answer
        

nums = [3,2,4]
target = 6
print(twoSum(nums, target))