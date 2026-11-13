# Count Non-Decreasing Subarrays After K Operations

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given an array `nums` of `n` integers and an integer `k`.

For each subarray of `nums`, you can apply  **up to**  `k` operations on it. In each operation, you increment any element of the subarray by 1.

 **Note**  that each subarray is considered independently, meaning changes made to one subarray do not persist to another.

Return the number of subarrays that you can make  **non-decreasing**  ​​​​​after performing at most `k` operations.

An array is said to be  **non-decreasing**  if each element is greater than or equal to its previous element, if it exists.

 

Original
Python
 **Example 1:** 

 **Input:**  nums = [6,3,1,2,4,4], k = 7

 **Output:**  17

 **Explanation:** 

Out of all 21 possible subarrays of `nums`, only the subarrays `[6, 3, 1]`, `[6, 3, 1, 2]`, `[6, 3, 1, 2, 4]` and `[6, 3, 1, 2, 4, 4]` cannot be made non-decreasing after applying up to k = 7 operations. Thus, the number of non-decreasing subarrays is `21 - 4 = 17`.

 **Example 2:** 

 **Input:**  nums = [6,3,1,3,6], k = 4

 **Output:**  12

 **Explanation:** 

The subarray `[3, 1, 3, 6]` along with all subarrays of `nums` with three or fewer elements, except `[6, 3, 1]`, can be made non-decreasing after `k` operations. There are 5 subarrays of a single element, 4 subarrays of two elements, and 2 subarrays of three elements except `[6, 3, 1]`, so there are `1 + 5 + 4 + 2 = 12` subarrays that can be made non-decreasing.

 

 **Constraints:** 

- 1 <= nums.length <= 105
- 1 <= nums[i] <= 109
- 1 <= k <= 109

## Solution

**Language:** Python  
**Runtime:** 495 ms (beats 57.14%)  
**Memory:** 30.5 MB (beats 42.86%)  
**Submitted:** 2026-11-13T03:22:35.754Z  

```py
from collections import deque

class Solution(object):
    def countNonDecreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        ans = 0
        cost = 0
        r = n - 1
        # Monotonic decreasing deque storing pairs of [value, count]
        q = deque()
        
        for l in range(n - 1, -1, -1):
            curr = nums[l]
            count = 1
            
            # Merge all elements to the right that are smaller than nums[l]
            while q and q[0][0] < curr:
                val, cnt = q.popleft()
                # Increasing these `cnt` elements from `val` to `curr` adds cost
                cost += (curr - val) * cnt
                count += cnt
                
            q.appendleft([curr, count])
            
            # Shrink the window from the right while operations exceed k
            while cost > k:
                # Subtract the cost contribution of the rightmost element
                cost -= q[-1][0] - nums[r]
                q[-1][1] -= 1
                if q[-1][1] == 0:
                    q.pop()
                r -= 1
                
            # All subarrays starting at l and ending between l and r are valid
            ans += r - l + 1
            
        return ans

```

---

[View on LeetCode](https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/)