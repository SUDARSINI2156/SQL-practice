# Minimum Swaps to Sort by Digit Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an array `nums` of  **distinct**  positive integers. You need to sort the array in  **increasing**  order based on the sum of the digits of each number. If two numbers have the same digit sum, the  **smaller**  number appears first in the sorted order.

Return the  **minimum**  number of swaps required to rearrange `nums` into this sorted order.

A  **swap**  is defined as exchanging the values at two distinct positions in the array.

 

 **Example 1:** 

 **Input:**  nums = [37,100]

 **Output:**  1

 **Explanation:** 

- Compute the digit sum for each integer: [3 + 7 = 10, 1 + 0 + 0 = 1] → [10, 1]
- Sort the integers based on digit sum: [100, 37]. Swap 37 with 100 to obtain the sorted order.
- Thus, the minimum number of swaps required to rearrange nums is 1.

 **Example 2:** 

 **Input:**  nums = [22,14,33,7]

 **Output:**  0

 **Explanation:** 

- Compute the digit sum for each integer: [2 + 2 = 4, 1 + 4 = 5, 3 + 3 = 6, 7 = 7] → [4, 5, 6, 7]
- Sort the integers based on digit sum: [22, 14, 33, 7]. The array is already sorted.
- Thus, the minimum number of swaps required to rearrange nums is 0.

 **Example 3:** 

 **Input:**  nums = [18,43,34,16]

 **Output:**  2

 **Explanation:** 

- Compute the digit sum for each integer: [1 + 8 = 9, 4 + 3 = 7, 3 + 4 = 7, 1 + 6 = 7] → [9, 7, 7, 7]
- Sort the integers based on digit sum: [16, 34, 43, 18]. Swap 18 with 16, and swap 43 with 34 to obtain the sorted order.
- Thus, the minimum number of swaps required to rearrange nums is 2.

 

 **Constraints:** 

- 1 <= nums.length <= 105
- 1 <= nums[i] <= 109
- nums consists of distinct positive integers.

## Solution

**Language:** Python  
**Runtime:** 1929 ms (beats 60.00%)  
**Memory:** 45.1 MB (beats 60.00%)  
**Submitted:** 2026-10-17T15:30:31.055Z  

```py
class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get_digit_sum(n):
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s
        
        # 1. Pair each number with its original index and sort by custom criteria
        # Priority 1: Digit sum (increasing)
        # Priority 2: Actual value (increasing)
        indexed_nums = [(num, idx) for idx, num in enumerate(nums)]
        indexed_nums.sort(key=lambda x: (get_digit_sum(x[0]), x[0]))
        
        # 2. Track visited positions to find graph cycles
        n = len(nums)
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            # If already visited or already in the correct position, skip
            if visited[i] or indexed_nums[i][1] == i:
                continue
                
            # Calculate the size of the current cycle
            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                # Move to the original index of the element currently occupying this position
                curr = indexed_nums[curr][1]
                cycle_size += 1
                
            # If cycle_size > 0, it contributes (cycle_size - 1) swaps
            if cycle_size > 0:
                swaps += (cycle_size - 1)
                
        return swaps

```

---

[View on LeetCode](https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/)