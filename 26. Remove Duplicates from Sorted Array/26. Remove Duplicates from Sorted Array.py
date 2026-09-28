def removeDuplicates( nums: list[int]) -> int:

    i = len(nums) - 1
    while i > 0:
        if nums[i] == nums[i - 1]:

            nums.pop(i)

        i -= 1
    
    k = len(nums)
    return k, nums

print(removeDuplicates([1,1,2]))

