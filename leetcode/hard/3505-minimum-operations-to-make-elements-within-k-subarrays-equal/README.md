# Minimum Operations to Make Elements Within K Subarrays Equal

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given an integer array `nums` and two integers, `x` and `k`. You can perform the following operation any number of times (**including zero**):

- Increase or decrease any element of nums by 1.

Return the  **minimum**  number of operations needed to have  **at least**  `k`  *non-overlapping subarrays*  of size  **exactly**  `x` in `nums`, where all elements within each subarray are equal.

 

 **Example 1:** 

 **Input:**  nums = [5,-2,1,3,7,3,6,4,-1], x = 3, k = 2

 **Output:**  8

 **Explanation:** 

- Use 3 operations to add 3 to nums[1] and use 2 operations to subtract 2 from nums[3]. The resulting array is [5, 1, 1, 1, 7, 3, 6, 4, -1].
- Use 1 operation to add 1 to nums[5] and use 2 operations to subtract 2 from nums[6]. The resulting array is [5, 1, 1, 1, 7, 4, 4, 4, -1].
- Now, all elements within each subarray [1, 1, 1] (from indices 1 to 3) and [4, 4, 4] (from indices 5 to 7) are equal. Since 8 total operations were used, 8 is the output.

 **Example 2:** 

 **Input:**  nums = [9,-2,-2,-2,1,5], x = 2, k = 2

 **Output:**  3

 **Explanation:** 

- Use 3 operations to subtract 3 from nums[4]. The resulting array is [9, -2, -2, -2, -2, 5].
- Now, all elements within each subarray [-2, -2] (from indices 1 to 2) and [-2, -2] (from indices 3 to 4) are equal. Since 3 operations were used, 3 is the output.

 

 **Constraints:** 

- 2 <= nums.length <= 105
- -106 <= nums[i] <= 106
- 2 <= x <= nums.length
- 1 <= k <= 15
- 2 <= k * x <= nums.length

## Solution

**Language:** Python  
**Runtime:** 8890 ms (beats 33.33%)  
**Memory:** 30.5 MB (beats 100.00%)  
**Submitted:** 2026-11-04T07:13:22.621Z  

```py

from sortedcontainers import SortedList

class Solution(object):
    def minOperations(self, nums, x, k):
        """
        :type nums: List[int]
        :type x: int
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if k * x > n:
            return -1
        
        left = SortedList()
        right = SortedList()
        
        # Using a list to hold mutable state integers to bypass Python 2 scoping limits
        sums = [0, 0] # [left_sum, right_sum]
        left_size = x // 2
        
        # 1. Precompute costs for all possible windows of size x
        C = []
        for i in range(n):
            # Inline Add logic
            item = (nums[i], i)
            val = item[0]
            if not left or item <= left[-1]:
                left.add(item)
                sums[0] += val
            else:
                right.add(item)
                sums[1] += val
                
            if i >= x:
                # Inline Remove logic
                rem_item = (nums[i - x], i - x)
                rem_val = rem_item[0]
                if rem_item in left:
                    left.remove(rem_item)
                    sums[0] -= rem_val
                else:
                    right.remove(rem_item)
                    sums[1] -= rem_val
            
            # Inline Balance logic
            while len(left) > left_size:
                pop_item = left.pop(-1)
                sums[0] -= pop_item[0]
                right.add(pop_item)
                sums[1] += pop_item[0]
            while len(left) < left_size and right:
                pop_item = right.pop(0)
                sums[1] -= pop_item[0]
                left.add(pop_item)
                sums[0] += pop_item[0]
                
            if i >= x - 1:
                med = right[0][0]
                cost = (sums[1] - len(right) * med) + (len(left) * med - sums[0])
                C.append(cost)
                
        # 2. Dynamic Programming to find the optimal k choices
        dp = [0] * (n + 1)
        
        for _ in range(k):
            next_dp = [float('inf')] * (n + 1)
            for j in range(x, n + 1):
                next_dp[j] = next_dp[j - 1]
                if dp[j - x] != float('inf'):
                    next_dp[j] = min(next_dp[j], dp[j - x] + C[j - x])
            dp = next_dp
                    
        return dp[n]

```

---

[View on LeetCode](https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/)