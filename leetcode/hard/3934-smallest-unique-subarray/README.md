# Smallest Unique Subarray

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given an integer array `nums`.

Find the  **minimum** length of a subarray that is  **not**   **identical**  to any other  **subarray**  in `nums`.

Return an integer denoting the  **minimum possible length**  of such a  **subarray**.

Two  **subarrays**  are considered identical if they have the same length and the same elements in corresponding positions.

 

Original
Python
 **Example 1:** 

 **Input:**  nums = [3,3,3]

 **Output:**  3

 **Explanation:** 

- Subarrays of length 1: [3] → appears 3 times
- Subarrays of length 2: [3, 3] → appears 2 times
- Subarrays of length 3: [3, 3, 3] → appears once

The subarray `[3, 3, 3]` is unique, so the smallest unique subarray length is 3.

 **Example 2:** 

 **Input:**  nums = [2,1,2,3,3]

 **Output:**  1

 **Explanation:** 

Subarrays of length 1:

- [2] → appears 2 times
- [1] → appears once
- [3] → appears 2 times
The subarray `[1]` is unique, so the smallest unique subarray length is 1.

 **Example 3:** 

 **Input:**  nums = [1,1,2,2,1]

 **Output:**  2

 **Explanation:** 

Subarrays of length 1:

- [1] → appears 3 times
- [2] → appears 2 times

Subarrays of length 2:

- [1, 1] → appears once
- [1, 2] → appears once
- [2, 2] → appears once
- [2, 1] → appears once
There is at least one subarray of length 2 that is unique, so the smallest unique subarray length is 2.

 

 **Constraints:** 

- 1 <= nums.length <= 105
- 1 <= nums[i] <= 105

## Solution

**Language:** Python  
**Runtime:** 4467 ms (beats 14.29%)  
**Memory:** 46.5 MB (beats 57.14%)  
**Submitted:** 2026-11-25T08:49:07.415Z  

```py
from collections import Counter

class Solution(object):
    def smallestUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # Double hashing constants to virtually eliminate hash collisions
        BASE1, MOD1 = 1315423911, 10**9 + 7
        BASE2, MOD2 = 2654435761, 10**9 + 9
        
        # Shift values by +1 in case nums contains 0 or negative numbers
        # (Alternatively, map numbers to positive ranks if negatives exist)
        min_val = min(nums)
        arr = [x - min_val + 1 for x in nums]

        def has_unique_subarray(length):
            h1 = h2 = 0
            p1 = pow(BASE1, length - 1, MOD1)
            p2 = pow(BASE2, length - 1, MOD2)
            
            # Build hash for the first window of size `length`
            for i in range(length):
                h1 = (h1 * BASE1 + arr[i]) % MOD1
                h2 = (h2 * BASE2 + arr[i]) % MOD2
                
            counts = Counter([(h1, h2)])
            
            # Slide the window across the rest of the array in O(1) per step
            for i in range(length, n):
                # Remove leftmost element
                h1 = (h1 - arr[i - length] * p1) % MOD1
                h2 = (h2 - arr[i - length] * p2) % MOD2
                
                # Shift and add new rightmost element
                h1 = (h1 * BASE1 + arr[i]) % MOD1
                h2 = (h2 * BASE2 + arr[i]) % MOD2
                
                counts[(h1, h2)] += 1
                
            return 1 in counts.values()

        # Binary search for the smallest valid length
        left, right = 1, n
        ans = n
        while left <= right:
            mid = (left + right) // 2
            if has_unique_subarray(mid):
                ans = mid
                right = mid - 1  # Try to find an even smaller length
            else:
                left = mid + 1   # Need a longer subarray to make it unique
                
        return ans

```

---

[View on LeetCode](https://leetcode.com/problems/smallest-unique-subarray/)