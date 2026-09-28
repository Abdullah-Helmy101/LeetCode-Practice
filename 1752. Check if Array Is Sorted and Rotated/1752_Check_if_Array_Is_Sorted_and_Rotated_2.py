from typing import List

def check(nums: List[int]) -> bool:

    count = 0 
    N = len(nums) - 1

    for i in range (N):
        if nums[N] > nums[(i + 1) % N]:
            count += 1

    return count <= 1   