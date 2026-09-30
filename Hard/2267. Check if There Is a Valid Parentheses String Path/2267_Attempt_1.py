def hasValidPath(self, grid: list[list[str]]) -> bool:
    
    m = len(grid)
    n = len(grid[0])
    

grid = [["(","(","("],
        [")","(",")"],
        ["(","(",")"],
        ["(","(",")"]]

count = sum(row.count('(') for row in grid)
print(count)