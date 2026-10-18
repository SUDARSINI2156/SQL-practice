# Number of Ways to Reorder Array to Get Same BST

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given an array `nums` that represents a permutation of integers from `1` to `n`. We are going to construct a binary search tree (BST) by inserting the elements of `nums` in order into an initially empty BST. Find the number of different ways to reorder `nums` so that the constructed BST is identical to that formed from the original array `nums`.

- For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, and 3 as a right child. The array [2,3,1] also yields the same BST but [3,2,1] yields a different BST.

Return  *the number of ways to reorder*  `nums`  *such that the BST formed is identical to the original BST formed from*  `nums`.

Since the answer may be very large,  **return it modulo** `109 + 7`.

 

 **Example 1:** 

```
Input: nums = [2,1,3]
Output: 1
Explanation: We can reorder nums to be [2,3,1] which will yield the same BST. There are no other ways to reorder nums which will yield the same BST.

```

 **Example 2:** 

```
Input: nums = [3,4,5,1,2]
Output: 5
Explanation: The following 5 arrays will yield the same BST: 
[3,1,2,4,5]
[3,1,4,2,5]
[3,1,4,5,2]
[3,4,1,2,5]
[3,4,1,5,2]

```

 **Example 3:** 

```
Input: nums = [1,2,3]
Output: 0
Explanation: There are no other orderings of nums that will yield the same BST.

```

 

 **Constraints:** 

- 1 <= nums.length <= 1000
- 1 <= nums[i] <= nums.length
- All integers in nums are distinct.

## Solution

**Language:** Python  
**Runtime:** 72 ms (beats 94.44%)  
**Memory:** 17.8 MB (beats 77.78%)  
**Submitted:** 2026-10-18T11:55:10.000Z  

```py
import math

class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # Python 2 fallback for math.comb(n, k)
        def nCr(n, r):
            if r < 0 or r > n:
                return 0
            if r == 0 or r == n:
                return 1
            if r > n // 2:
                r = n - r
            # Efficiently compute combinations inline
            numerator = 1
            denominator = 1
            for i in range(r):
                numerator *= (n - i)
                denominator *= (i + 1)
            return numerator // denominator
        
        def dfs(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            
            # Using the helper function instead of math.comb
            interleave_ways = nCr(len(left) + len(right), len(left))
            
            return (interleave_ways * dfs(left) * dfs(right)) % MOD
        
        return (dfs(nums) - 1) % MOD


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
```

---

[View on LeetCode](https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/)