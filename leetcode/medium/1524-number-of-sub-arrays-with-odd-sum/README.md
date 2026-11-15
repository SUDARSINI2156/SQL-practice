# Number of Sub-arrays With Odd Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array of integers `arr`, return  *the number of subarrays with an  **odd**  sum*.

Since the answer can be very large, return it modulo `109 + 7`.

 

Original
Python
 **Example 1:** 

```
Input: arr = [1,3,5]
Output: 4
Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.

```

 **Example 2:** 

```
Input: arr = [2,4,6]
Output: 0
Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.

```

 **Example 3:** 

```
Input: arr = [1,2,3,4,5,6,7]
Output: 16

```

 

 **Constraints:** 

- 1 <= arr.length <= 105
- 1 <= arr[i] <= 100

## Solution

**Language:** Python  
**Runtime:** 79 ms (beats 49.23%)  
**Memory:** 15.1 MB (beats 96.92%)  
**Submitted:** 2026-11-15T06:12:44.651Z  

```py
class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        
        odd_count = 0
        even_count = 1  # Empty prefix sum (0) is even
        prefix_sum = 0
        result = 0
        
        for num in arr:
            prefix_sum += num
            
            if prefix_sum % 2 == 1:
                # Odd prefix sum pairs with all previous even prefix sums
                result = (result + even_count) % MOD
                odd_count += 1
            else:
                # Even prefix sum pairs with all previous odd prefix sums
                result = (result + odd_count) % MOD
                even_count += 1
                
        return result

```

---

[View on LeetCode](https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/)