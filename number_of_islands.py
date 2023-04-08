from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        count = 0

        def dfs(r, c):
            if ((r not in range(ROWS)) or
                (c not in range(COLS)) or
                ((r, c) in visited)
                    or grid[r][c] == '0'):
                return
            visited.add((r, c))
            direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in direction:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visited:
                    count += 1
                    dfs(r, c)

        return count


sol = Solution()
print(sol.numIslands([
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))
print(sol.numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
