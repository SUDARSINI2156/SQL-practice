# Minimum Score by Changing Two Elements

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an integer array `nums`.

- The low score of nums is the minimum absolute difference between any two integers.
- The high score of nums is the maximum absolute difference between any two integers.
- The score of nums is the sum of the high and low scores.

Return the  **minimum score**  after  **changing two elements**  of `nums`.

 

Original
Python
 **Example 1:** 

 **Input:**  nums = [1,4,7,8,5]

 **Output:**  3

 **Explanation:** 

- Change nums[0] and nums[1] to be 6 so that nums becomes [6,6,7,8,5].
- The low score is the minimum absolute difference: |6 - 6| = 0.
- The high score is the maximum absolute difference: |8 - 5| = 3.
- The sum of high and low score is 3.

 **Example 2:** 

 **Input:**  nums = [1,4,3]

 **Output:**  0

 **Explanation:** 

- Change nums[1] and nums[2] to 1 so that nums becomes [1,1,1].
- The sum of maximum absolute difference and minimum absolute difference is 0.

 

 **Constraints:** 

- 3 <= nums.length <= 105
- 1 <= nums[i] <= 109

## Solution

**Language:** Python  
**Runtime:** 48 ms (beats 54.55%)  
**Memory:** 19.8 MB (beats 18.18%)  
**Submitted:** 2026-11-19T12:08:40.221Z  

```py
class Solution(object):
    def minimizeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        # Option 1: Change the two smallest elements
        change_two_smallest = nums[-1] - nums[2]
        
        # Option 2: Change the two largest elements
        change_two_largest = nums[-3] - nums[0]
        
        # Option 3: Change one smallest and one largest element
        change_both_ends = nums[-2] - nums[1]
        
        return min(change_two_smallest, change_two_largest, change_both_ends)

```

---

[View on LeetCode](https://leetcode.com/problems/minimum-score-by-changing-two-elements/)