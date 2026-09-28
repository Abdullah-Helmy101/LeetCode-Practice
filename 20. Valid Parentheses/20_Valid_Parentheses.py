def isValid(s: str) -> bool:
    
    bracket_map = {")": "(", "}": "{", "]": "["}
    stack = []

    for c in s:
        if c in bracket_map:

            top_element = stack.pop() if stack else '#'

            if bracket_map[c] != top_element:
                return False
            
        else:
            stack.append(c)

    return not stack

print(isValid('[)'))