# Climbing Stairs II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are climbing a staircase with `n + 1` steps, numbered from 0 to `n`.

You are also given a  **1-indexed**  integer array `costs` of length `n`, where `costs[i]` is the cost of step `i`.

From step `i`, you can jump  **only**  to step `i + 1`, `i + 2`, or `i + 3`. The cost of jumping from step `i` to step `j` is defined as: `costs[j] + (j - i)2`

You start from step 0 with `cost = 0`.

Return the  **minimum**  total cost to reach step `n`.

 

Original
Python
 **Example 1:** 

 **Input:**  n = 4, costs = [1,2,3,4]

 **Output:**  13

 **Explanation:** 

One optimal path is `0 → 1 → 2 → 4`

Jump	Cost Calculation	Cost
0 → 1	`costs[1] + (1 - 0)2 = 1 + 1`	2
1 → 2	`costs[2] + (2 - 1)2 = 2 + 1`	3
2 → 4	`costs[4] + (4 - 2)2 = 4 + 4`	8

Thus, the minimum total cost is `2 + 3 + 8 = 13`

 **Example 2:** 

 **Input:**  n = 4, costs = [5,1,6,2]

 **Output:**  11

 **Explanation:** 

One optimal path is `0 → 2 → 4`

Jump	Cost Calculation	Cost
0 → 2	`costs[2] + (2 - 0)2 = 1 + 4`	5
2 → 4	`costs[4] + (4 - 2)2 = 2 + 4`	6

Thus, the minimum total cost is `5 + 6 = 11`

 **Example 3:** 

 **Input:**  n = 3, costs = [9,8,3]

 **Output:**  12

 **Explanation:** 

The optimal path is `0 → 3` with total cost = `costs[3] + (3 - 0)2 = 3 + 9 = 12`

 

 **Constraints:** 

- 1 <= n == costs.length <= 105​​​​​​​
- 1 <= costs[i] <= 104

## Solution

**Language:** Python  
**Runtime:** 272 ms (beats 85.45%)  
**Memory:** 20.8 MB (beats 96.36%)  
**Submitted:** 2026-11-10T16:56:22.877Z  

```py
class Solution(object):
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        # Track the minimum costs for steps: j-3, j-2, and j-1
        # Initially, step 0 has cost 0, and out-of-bounds steps are infinity
        prev3 = float('inf')  # Represents dp[j - 3]
        prev2 = float('inf')  # Represents dp[j - 2]
        prev1 = 0             # Represents dp[0]
        
        for j in range(1, n + 1):
            # Calculate the minimum cost to jump to step j from valid prior steps
            jump1 = prev1 + 1
            jump2 = prev2 + 4
            jump3 = prev3 + 9
            
            # costs is 0-indexed in Python, so step j corresponds to costs[j - 1]
            curr = costs[j - 1] + min(jump1, jump2, jump3)
            
            # Shift the rolling variables forward for the next step
            prev3, prev2, prev1 = prev2, prev1, curr
            
        return prev1

```

---

[View on LeetCode](https://leetcode.com/problems/climbing-stairs-ii/)