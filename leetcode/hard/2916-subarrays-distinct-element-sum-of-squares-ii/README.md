# Subarrays Distinct Element Sum of Squares II

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given a  **0-indexed** integer array `nums`.

The  **distinct count**  of a subarray of `nums` is defined as:

- Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].

Return  *the sum of the  **squares**  of  **distinct counts**  of all subarrays of* `nums`.

Since the answer may be very large, return it  **modulo**  `109 + 7`.

A subarray is a contiguous  **non-empty**  sequence of elements within an array.

 

 **Example 1:** 

```
Input: nums = [1,2,1]
Output: 15
Explanation: Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 + 22 + 22 + 22 = 15.

```

 **Example 2:** 

```
Input: nums = [2,2]
Output: 3
Explanation: Three possible subarrays are:
[2]: 1 distinct value
[2]: 1 distinct value
[2,2]: 1 distinct value
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 = 3.
```

 

 **Constraints:** 

- 1 <= nums.length <= 105
- 1 <= nums[i] <= 105

## Solution

**Language:** Python  
**Runtime:** 8200 ms (beats 12.50%)  
**Memory:** 100.4 MB (beats 25.00%)  
**Submitted:** 2026-10-16T03:38:18.177Z  

```py
class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        MOD = 10**9 + 7
        
        # Segment tree arrays (size 4 * n)
        # sum_sq stores the sum of squares of distinct counts
        # sum_val stores the sum of distinct counts (needed for expanding (x+1)^2 = x^2 + 2x + 1)
        sum_sq = [0] * (4 * n)
        sum_val = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def push(node, start, end):
            if lazy[node] == 0:
                return
            
            lazy_val = lazy[node]
            mid = (start + end) // 2
            
            # Left child update
            left_len = mid - start + 1
            sum_sq[2 * node] = (sum_sq[2 * node] + 2 * lazy_val * sum_val[2 * node] + lazy_val * lazy_val * left_len) % MOD
            sum_val[2 * node] = (sum_val[2 * node] + lazy_val * left_len) % MOD
            lazy[2 * node] += lazy_val
            
            # Right child update
            right_len = end - mid
            sum_sq[2 * node + 1] = (sum_sq[2 * node + 1] + 2 * lazy_val * sum_val[2 * node + 1] + lazy_val * lazy_val * right_len) % MOD
            sum_val[2 * node + 1] = (sum_val[2 * node + 1] + lazy_val * right_len) % MOD
            lazy[2 * node + 1] += lazy_val
            
            lazy[node] = 0

        def update(node, start, end, l, r, val):
            if r < start or end < l:
                return
            if l <= start and end <= r:
                length = end - start + 1
                sum_sq[node] = (sum_sq[node] + 2 * val * sum_val[node] + val * val * length) % MOD
                sum_val[node] = (sum_val[node] + val * length) % MOD
                lazy[node] += val
                return
                
            push(node, start, end)
            mid = (start + end) // 2
            update(2 * node, start, mid, l, r, val)
            update(2 * node + 1, mid + 1, end, l, r, val)
            
            sum_sq[node] = (sum_sq[2 * node] + sum_sq[2 * node + 1]) % MOD
            sum_val[node] = (sum_val[2 * node] + sum_val[2 * node + 1]) % MOD

        total_sum = 0
        last_pos = {}
        
        for j in range(n):
            # Find the last occurrence of the current element
            prev_idx = last_pos.get(nums[j], -1)
            
            # Increment distinct counts for all valid left endpoints in range [prev_idx + 1, j]
            update(1, 0, n - 1, prev_idx + 1, j, 1)
            
            # The root node (index 1) maintains the total sum of squares for all subarrays ending at index j
            total_sum = (total_sum + sum_sq[1]) % MOD
            
            # Update the latest seen position of this element
            last_pos[nums[j]] = j
            
        return total_sum


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
```

---

[View on LeetCode](https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/)