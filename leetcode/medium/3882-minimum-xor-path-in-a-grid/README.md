# Minimum XOR Path in a Grid

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a 2D integer array `grid` of size `m * n`.

You start at the  **top-left**  cell `(0, 0)` and want to reach the  **bottom-right**  cell `(m - 1, n - 1)`.

At each step, you  **may**  move either  **right or down**.

The  **cost**  of a path is defined as the  **bitwise XOR**  of all the values in the cells along that path,  **including**  the start and end cells.

Return the  **minimum**  possible XOR value among all valid paths from `(0, 0)` to `(m - 1, n - 1)`.

 

 **Example 1:** 

 **Input:**  grid = [[1,2],[3,4]]

 **Output:**  6

 **Explanation:** 

There are two valid paths:

- (0, 0) → (0, 1) → (1, 1) with XOR: 1 XOR 2 XOR 4 = 7
- (0, 0) → (1, 0) → (1, 1) with XOR: 1 XOR 3 XOR 4 = 6

The minimum XOR value among all valid paths is 6.

 **Example 2:** 

 **Input:**  grid = [[6,7],[5,8]]

 **Output:**  9

 **Explanation:** 

There are two valid paths:

- (0, 0) → (0, 1) → (1, 1) with XOR: 6 XOR 7 XOR 8 = 9
- (0, 0) → (1, 0) → (1, 1) with XOR: 6 XOR 5 XOR 8 = 11

The minimum XOR value among all valid paths is 9.

 **Example 3:** 

 **Input:**  grid = [[2,7,5]]

 **Output:**  0

 **Explanation:** 

There is only one valid path:

- (0, 0) → (0, 1) → (0, 2) with XOR: 2 XOR 7 XOR 5 = 0

The XOR value of this path is 0, which is the minimum possible.

 

 **Constraints:** 

- 1 <= m == grid.length <= 1000
- 1 <= n == grid[i].length <= 1000
- m * n <= 1000
- 0 <= grid[i][j] <= 1023​

## Solution

**Language:** Python  
**Runtime:** 732 ms (beats 100.00%)  
**Memory:** 18.3 MB (beats 77.78%)  
**Submitted:** 2026-10-28T06:15:03.728Z  

```py
class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        # dp[j] stores the set of all achievable XOR values at column j for the current row
        dp = [set() for _ in range(n)]
        
        # Base case: Starting point (0, 0)
        dp[0].add(grid[0][0])
        
        # Initialize the first row (can only come from the left)
        for j in range(1, n):
            val = grid[0][j]
            dp[j] = {x ^ val for x in dp[j-1]}
            
        # Fill the rest of the DP table row by row
        for i in range(1, m):
            # First column of the current row (can only come from above)
            val = grid[i][0]
            dp[0] = {x ^ val for x in dp[0]}
            
            # Remaining columns (can come from above or from the left)
            for j in range(1, n):
                val = grid[i][j]
                combined_previous_states = dp[j] | dp[j-1]
                dp[j] = {x ^ val for x in combined_previous_states}
                
        # The answer is the minimum value in the final cell's set
        return min(dp[n-1])


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-xor-path-in-a-grid/)