from typing import List

def is_sorted(nums: List[int]):

    return all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))

def rotate(nums: List[int], x: int):
    N = len(nums)
    return [nums[(i + x) % N] for i in range(N)]


def check(nums: List[int]) -> bool:
    
    if is_sorted(nums):

        return True
    
    index = nums.index(min(nums))
    
    minimum_val = index if index > 0 else index + 1

    return rotate(nums, minimum_val)


print(check([3,4,5,1,2]))