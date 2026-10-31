# Twisted Mirror Path Count

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an `m x n` binary grid `grid` where:

- grid[i][j] == 0 represents an empty cell, and
- grid[i][j] == 1 represents a mirror.

A robot starts at the top-left corner of the grid `(0, 0)` and wants to reach the bottom-right corner `(m - 1, n - 1)`. It can move only  **right**  or  **down**. If the robot attempts to move into a mirror cell, it is  **reflected**  before entering that cell:

- If it tries to move right into a mirror, it is turned down and moved into the cell directly below the mirror.
- If it tries to move down into a mirror, it is turned right and moved into the cell directly to the right of the mirror.

If this reflection would cause the robot to move outside the `grid` boundaries, the path is considered invalid and should not be counted.

Return the number of unique valid paths from `(0, 0)` to `(m - 1, n - 1)`.

Since the answer may be very large, return it  **modulo**  `109 + 7`.

 **Note** : If a reflection moves the robot into a mirror cell, the robot is immediately reflected again based on the direction it used to enter that mirror: if it entered while moving right, it will be turned down; if it entered while moving down, it will be turned right. This process will continue until either the last cell is reached, the robot moves out of bounds or the robot moves to a non-mirror cell.

 

 **Example 1:** 

 **Input:**  grid = [[0,1,0],[0,0,1],[1,0,0]]

 **Output:**  5

 **Explanation:** 

Number	Full Path
1	(0, 0) → (0, 1) [M] → (1, 1) → (1, 2) [M] → (2, 2)
2	(0, 0) → (0, 1) [M] → (1, 1) → (2, 1) → (2, 2)
3	(0, 0) → (1, 0) → (1, 1) → (1, 2) [M] → (2, 2)
4	(0, 0) → (1, 0) → (1, 1) → (2, 1) → (2, 2)
5	(0, 0) → (1, 0) → (2, 0) [M] → (2, 1) → (2, 2)
- [M] indicates the robot attempted to enter a mirror cell and instead reflected.

 **Example 2:** 

 **Input:**  grid = [[0,0],[0,0]]

 **Output:**  2

 **Explanation:** 

Number	Full Path
1	(0, 0) → (0, 1) → (1, 1)
2	(0, 0) → (1, 0) → (1, 1)

 **Example 3:** 

 **Input:**  grid = [[0,1,1],[1,1,0]]

 **Output:**  1

 **Explanation:** 

Number	Full Path
1	(0, 0) → (0, 1) [M] → (1, 1) [M] → (1, 2)
`(0, 0) → (1, 0) [M] → (1, 1) [M] → (2, 1)` goes out of bounds, so it is invalid.

 

 **Constraints:** 

- m == grid.length
- n == grid[i].length
- 2 <= m, n <= 500
- grid[i][j] is either 0 or 1.
- grid[0][0] == grid[m - 1][n - 1] == 0

## Solution

**Language:** Python  
**Runtime:** 1702 ms (beats 72.73%)  
**Memory:** 31.3 MB (beats 81.82%)  
**Submitted:** 2026-10-31T13:37:57.707Z  

```py
class Solution(object):
    def uniquePaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        MOD = 10**9 + 7
        
        # dp_right[i][j]: Ways to enter cell (i, j) while moving RIGHT
        # dp_down[i][j]: Ways to enter cell (i, j) while moving DOWN
        dp_right = [[0] * n for _ in range(m)]
        dp_down = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                # 1. Starting condition at (0, 0)
                if i == 0 and j == 0:
                    if j + 1 < n:
                        dp_right[i][j+1] = (dp_right[i][j+1] + 1) % MOD
                    if i + 1 < m:
                        dp_down[i+1][j] = (dp_down[i+1][j] + 1) % MOD
                
                # 2. Case: The robot successfully landed on an empty cell
                elif grid[i][j] == 0:
                    total_here = (dp_right[i][j] + dp_down[i][j]) % MOD
                    # From an empty cell, the robot can choose to go either RIGHT or DOWN
                    if j + 1 < n:
                        dp_right[i][j+1] = (dp_right[i][j+1] + total_here) % MOD
                    if i + 1 < m:
                        dp_down[i+1][j] = (dp_down[i+1][j] + total_here) % MOD
                
                # 3. Case: The robot hit a mirror cell
                else:
                    # If it entered while moving RIGHT, it is deflected DOWNwards
                    if i + 1 < m:
                        dp_down[i+1][j] = (dp_down[i+1][j] + dp_right[i][j]) % MOD
                    # If it entered while moving DOWN, it is deflected RIGHTwards
                    if j + 1 < n:
                        dp_right[i][j+1] = (dp_right[i][j+1] + dp_down[i][j]) % MOD
                        
        # The total number of valid ways to land successfully on the bottom-right corner
        return (dp_right[m-1][n-1] + dp_down[m-1][n-1]) % MOD

```

---

[View on LeetCode](https://leetcode.com/problems/twisted-mirror-path-count/)