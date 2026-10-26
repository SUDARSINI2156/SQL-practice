# Count Islands With Total Value Divisible by K

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an `m x n` matrix `grid` and a positive integer `k`. An  **island**  is a group of  **positive**  integers (representing land) that are  **4-directionally**  connected (horizontally or vertically).

The  **total value**  of an island is the sum of the values of all cells in the island.

Return the number of islands with a total value  **divisible by**  `k`.

 

 **Example 1:** 

 **Input:**  grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5

 **Output:**  2

 **Explanation:** 

The grid contains four islands. The islands highlighted in blue have a total value that is divisible by 5, while the islands highlighted in red do not.

 **Example 2:** 

 **Input:**  grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]], k = 3

 **Output:**  6

 **Explanation:** 

The grid contains six islands, each with a total value that is divisible by 3.

 

 **Constraints:** 

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 1000
- 1 <= m * n <= 105
- 0 <= grid[i][j] <= 106
- 1 <= k <= 106

## Solution

**Language:** Python  
**Runtime:** 452 ms (beats 70.59%)  
**Memory:** 21.7 MB (beats 58.82%)  
**Submitted:** 2026-10-26T03:28:55.012Z  

```py
class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
            
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        divisible_island_count = 0
        
        # Directions for 4-directional movement (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for i in range(m):
            for j in range(n):
                # A positive integer represents unvisited land
                if grid[i][j] > 0 and not visited[i][j]:
                    island_sum = 0
                    stack = [(i, j)]
                    visited[i][j] = True
                    
                    # Explore the full island iteratively
                    while stack:
                        r, c = stack.pop()
                        island_sum += grid[r][c]
                        
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            # Ensure bounds, evaluate land, and verify it hasn't been visited
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                stack.append((nr, nc))
                    
                    # Check if the complete island sum is divisible by k
                    if island_sum % k == 0:
                        divisible_island_count += 1
                        
        return divisible_island_count

```

---

[View on LeetCode](https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/)