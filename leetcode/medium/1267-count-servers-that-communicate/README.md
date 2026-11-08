# Count Servers that Communicate

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a map of a server center, represented as a `m * n` integer matrix `grid`, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

 

 **Example 1:** 

```
Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.
```

 **Example 2:** 

```
Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.

```

 **Example 3:** 

```
Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.

```

 

 **Constraints:** 

- m == grid.length
- n == grid[i].length
- 1 <= m <= 250
- 1 <= n <= 250
- grid[i][j] == 0 or 1

## Solution

**Language:** Python  
**Runtime:** 26 ms (beats 78.57%)  
**Memory:** 13.1 MB (beats 69.05%)  
**Submitted:** 2026-11-08T11:46:02.827Z  

```py
class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        row_cnt = [0] * m
        col_cnt = [0] * n
        
        # First pass: count servers in each row and column
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_cnt[i] += 1
                    col_cnt[j] += 1
                    
        # Second pass: count servers that share a row or column with another
        total_communicating = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row_cnt[i] > 1 or col_cnt[j] > 1):
                    total_communicating += 1
                    
        return total_communicating

```

---

[View on LeetCode](https://leetcode.com/problems/count-servers-that-communicate/)