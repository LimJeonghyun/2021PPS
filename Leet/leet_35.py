def searchInsert(nums, target):
    for i in range (len(nums)):
        if target <= nums[i]:
            return i
        elif target > nums[i]:
            if i+1 == len(nums) or target < nums[i+1] :
                return i+1
        
        # elif target < nums[i]:
        #     return i
        
nums = [1,3,5,6]
target = 2
print(searchInsert(nums, target))