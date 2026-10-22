# Minimum Operations to Sort a Permutation

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an integer array `nums` of length `n`, where `nums` is a permutation of the integers from 0 to `n - 1`.

You may perform  **only**  the following operations:

- Reverse the entire array.
- Rotate Left by One: Move the first element to the end of the array, and rest elements to left by one position.

Return an integer denoting the  **minimum**  number of operations required to sort the array in  **increasing**  order. If it is  **not possible**  to sort the array using only the given operations, return -1.

 

 **Example 1:** 

 **Input:**  nums = [0,2,1]

 **Output:**  2

 **Explanation:** 

- Rotate Left by one: [2, 1, 0]
- Reverse the array: [0, 1, 2]

The array becomes sorted in 2 operations, which is minimal

 **Example 2:** 

 **Input:**  nums = [1,0,2]

 **Output:**  2

 **Explanation:** 

- Reverse the array: [2, 0, 1]
- Rotate Left by one: [0, 1, 2]

The array becomes sorted in 2 operations, which is minimal.

 **Example 3:** 

 **Input:**  nums = [2,0,1,3]

 **Output:**  -1

 **Explanation:** 

It is impossible to reach `[2, 0, 1, 3]`. Thus, the answer is -1.

 

 **Constraints:** 

- 1 <= n == nums.length <= 105
- 0 <= nums[i] <= n - 1
- nums is a permutation of integers from 0 to n - 1.

## Solution

**Language:** Python  
**Runtime:** 81 ms (beats 57.14%)  
**Memory:** 21.5 MB (beats 71.43%)  
**Submitted:** 2026-10-22T04:24:11.149Z  

```py
class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        zero = nums.index(0)
        
        # Helper to verify if the cyclic permutation matches the expected direction
        def check(step):
            for i in range(n):
                if nums[(zero + i * step) % n] != i:
                    return False
            return True

        ans = float('inf')
        
        # Case 1: Increasing cyclic order
        if check(1):
            ans = min(ans, zero)          # Direct left rotations
            ans = min(ans, n - zero + 2)  # Reverse -> Rotate -> Reverse
            
        # Case 2: Decreasing cyclic order
        if check(-1):
            ans = min(ans, zero + 2)      # Rotate -> Reverse
            ans = min(ans, n - zero)      # Reverse -> Rotate
            
        return ans if ans != float('inf') else -1

```

---

[View on LeetCode](https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/)