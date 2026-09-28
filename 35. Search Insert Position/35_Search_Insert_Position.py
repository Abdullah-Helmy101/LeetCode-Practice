from typing import List

def searchInsert(nums: List[int], target: int) -> int:
  
    length = len(nums)

    if target in nums:
        return nums.index(target)

    if target < nums[0]:
        return 0

    for i in range(1, length):

        if nums[i - 1] < target < nums[i]:
            return i

    return length
    

print(searchInsert([1], 0))