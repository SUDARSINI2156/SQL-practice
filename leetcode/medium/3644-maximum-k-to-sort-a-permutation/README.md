# Maximum K to Sort a Permutation

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an integer array `nums` of length `n`, where `nums` is a  **permutation**  of the numbers in the range `[0..n - 1]`.

You may swap elements at indices `i` and `j`  **only if**  `nums[i] AND nums[j] == k`, where `AND` denotes the bitwise AND operation and `k` is a  **non-negative**  integer.

Return the  **maximum**  value of `k` such that the array can be sorted in  **non-decreasing**  order using any number of such swaps. If `nums` is already sorted, return 0.

 

 **Example 1:** 

 **Input:**  nums = [0,3,2,1]

 **Output:**  1

 **Explanation:** 

Choose `k = 1`. Swapping `nums[1] = 3` and `nums[3] = 1` is allowed since `nums[1] AND nums[3] == 1`, resulting in a sorted permutation: `[0, 1, 2, 3]`.

 **Example 2:** 

 **Input:**  nums = [0,1,3,2]

 **Output:**  2

 **Explanation:** 

Choose `k = 2`. Swapping `nums[2] = 3` and `nums[3] = 2` is allowed since `nums[2] AND nums[3] == 2`, resulting in a sorted permutation: `[0, 1, 2, 3]`.

 **Example 3:** 

 **Input:**  nums = [3,2,1,0]

 **Output:**  0

 **Explanation:** 

Only `k = 0` allows sorting since no greater `k` allows the required swaps where `nums[i] AND nums[j] == k`.

 

 **Constraints:** 

- 1 <= n == nums.length <= 105
- 0 <= nums[i] <= n - 1
- nums is a permutation of integers from 0 to n - 1.

## Solution

**Language:** Python  
**Runtime:** 45 ms (beats 16.67%)  
**Memory:** 22 MB (beats 0.00%)  
**Submitted:** 2026-10-23T04:06:31.308Z  

```py
class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Find all elements that are not in their sorted positions
        misplaced = [num for i, num in enumerate(nums) if num != i]
        
        # If the array is already sorted, return 0
        if not misplaced:
            return 0
        
        # Calculate the bitwise AND of all misplaced elements
        ans = misplaced[0]
        for num in misplaced[1:]:
            ans &= num
            
        return ans

```

---

[View on LeetCode](https://leetcode.com/problems/maximum-k-to-sort-a-permutation/)