# Maximum Subarray With Equal Products

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given an array of  **positive**  integers `nums`.

An array `arr` is called  **product equivalent**  if `prod(arr) == lcm(arr) * gcd(arr)`, where:

- prod(arr) is the product of all elements of arr.
- gcd(arr) is the GCD of all elements of arr.
- lcm(arr) is the LCM of all elements of arr.

Return the length of the  **longest**   **product equivalent**  subarray of `nums`.

 

Original
Python
 **Example 1:** 

 **Input:**  nums = [1,2,1,2,1,1,1]

 **Output:**  5

 **Explanation:**  

The longest product equivalent subarray is `[1, 2, 1, 1, 1]`, where `prod([1, 2, 1, 1, 1]) = 2`, `gcd([1, 2, 1, 1, 1]) = 1`, and `lcm([1, 2, 1, 1, 1]) = 2`.

 **Example 2:** 

 **Input:**  nums = [2,3,4,5,6]

 **Output:**  3

 **Explanation:**  

The longest product equivalent subarray is `[3, 4, 5].`

 **Example 3:** 

 **Input:**  nums = [1,2,3,1,4,5,1]

 **Output:**  5

 

 **Constraints:** 

- 2 <= nums.length <= 100
- 1 <= nums[i] <= 10

## Solution

**Language:** Python  
**Runtime:** 39 ms (beats 94.44%)  
**Memory:** 12.1 MB (beats 75.00%)  
**Submitted:** 2026-11-24T08:34:53.073Z  

```py
from fractions import gcd

class Solution(object):
    def maxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def lcm(a, b):
            return (a * b) // gcd(a, b)

        n = len(nums)
        ans = 0
        
        # Compute upper bound for any valid subarray product
        total_lcm = 1
        for x in nums:
            total_lcm = lcm(total_lcm, x)
        max_p = total_lcm * max(nums)

        for i in range(n):
            p, g, l = 1, 0, 1
            for j in range(i, n):
                p *= nums[j]
                g = gcd(g, nums[j])
                l = lcm(l, nums[j])
                
                if p == g * l:
                    ans = max(ans, j - i + 1)
                if p > max_p:
                    break
                    
        return ans

```

---

[View on LeetCode](https://leetcode.com/problems/maximum-subarray-with-equal-products/)