class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:

        n = len(nums)
        instability = []

        for i in range(0, n):
            largest = max(nums[:i+1])
            smallest = min(nums[i:])
            instability_score = largest - smallest

            if instability_score <= k:
                return i

        return -1

fsi = Solution()

print(fsi.firstStableIndex([5,0,1,4], 3))

            

    