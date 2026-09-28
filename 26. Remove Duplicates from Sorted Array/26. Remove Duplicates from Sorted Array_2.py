def removeDuplicates( nums: list[int]) -> int:

    k = 0
    for j in range(1, len(nums)):
        if nums[k] != nums[j]:
            k += 1
            nums[k] = nums[j]

    return k + 1, nums

print(removeDuplicates([1,1,2]))

