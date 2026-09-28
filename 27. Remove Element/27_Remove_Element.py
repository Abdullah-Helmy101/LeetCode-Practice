from typing import List
def removeElement(nums: List[int], val: int) -> int:
    
    k = 0
    i = len(nums) - 1

    while i >= 0:

        if nums[i] == val:

            nums.pop(i)
        else:

            k += 1

        i -= 1 

    return k, nums

print(removeElement([3,2,2,3], 3))