class Solution(object):
    def majorityElement(self, nums):
        sorting = list(set(nums))
        for each in sorting:
            if len(nums)/2 < nums.count(each):
                return each