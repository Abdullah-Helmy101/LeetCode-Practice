from typing import List

def canReach(arr: List[int], start: int) -> bool:
    
    stack = [start]
    visited = set()

    while stack:

        i = stack.pop()

        if i in visited:
            continue

        visited.add(i)
        
        if arr[i] == 0:
            return True
        
        right = i + arr[i]
        left = i - arr[i]

        if right < len(arr):
            stack.append(right)

        if left >+ 0:
            stack.append(left)
    
    return False

print(canReach(arr = [4,2,3,0,3,1,2], start = 5))