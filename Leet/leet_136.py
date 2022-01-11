def singleNumber(nums):
    tmp = list(set(nums))
    for i in range (len(tmp)):
        count=0
        # target = str(tmp[i])
        count = nums.count(tmp[i])
        if count == 1:
            singlenum = tmp[i]
            # singlenumlist.append(tmp[i])
    
    return singlenum

nums = [2,2,1]
print(singleNumber(nums))
        