class Solution:
    def maxDepth(self, s: str) -> int:

        depth = 0
        max_depth = 0

        for i in s:
            if i == '(':
                depth += 1

            elif i == ')':
                depth -= 1

            if depth > max_depth:
                max_depth = depth

        return max_depth



test = Solution()

print(test.maxDepth('(1+(2*3)+((8)/4))+1'))