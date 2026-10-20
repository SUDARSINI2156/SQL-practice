# Sum of Sortable Integers

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given an integer array `nums` of length `n`.

An integer `k` is called  **sortable**  if `k`  **divides**  `n` and you can sort `nums` in  **non-decreasing**  order by sequentially performing the following operations:

- Partition nums into consecutive subarrays of length k.
- Cyclically rotate each subarray independently any number of times to the left or to the right.

Return an integer denoting the sum of all possible sortable integers `k`.

 

 **Example 1:** 

 **Input:**  nums = [3,1,2]

 **Output:**  3

 **Explanation:** ​​​​​​​

- For n = 3, possible divisors are 1 and 3.
- For k = 1: each subarray has one element. No rotation can sort the array.
- For k = 3: the single subarray [3, 1, 2] can be rotated once to produce [1, 2, 3], which is sorted.
- Only k = 3 is sortable. Hence, the answer is 3.

 **Example 2:** 

 **Input:**  nums = [7,6,5]

 **Output:**  0

 **Explanation:** 

- For n = 3, possible divisors are 1 and 3.
- For k = 1: each subarray has one element. No rotation can sort the array.
- For k = 3: the single subarray [7, 6, 5] cannot be rotated into non-decreasing order.
- No k is sortable. Hence, the answer is 0.

 **Example 3:** 

 **Input:**  nums = [5,8]

 **Output:**  3

 **Explanation:** ​​​​​​​

- For n = 2, possible divisors are 1 and 2.
- Since [5, 8] is already sorted, every divisor is sortable. Hence, the answer is 1 + 2 = 3.

 

 **Constraints:** 

- 1 <= n == nums.length <= 105
- 1 <= nums[i] <= 105

## Solution

**Language:** Python  
**Runtime:** 2021 ms (beats 85.71%)  
**Memory:** 25.6 MB (beats 28.57%)  
**Submitted:** 2026-10-20T12:10:59.697Z  

```py
class Solution(object):
    def sortableIntegers(self, nums):
        """
        :type nums: List[int]
        :type : rtype: int
        """
        n = len(nums)
        S = sorted(nums)
        
        def check(k):
            for i in range(0, n, k):
                A = nums[i:i+k]
                B = S[i:i+k]
                
                drops = 0
                drop_idx = -1
                
                # Count drops with wrap-around
                for j in range(k):
                    if A[j] > A[(j + 1) % k]:
                        drops += 1
                        drop_idx = j
                        if drops > 1:
                            return False
                
                if drops == 0:
                    if A != B:
                        return False
                else:
                    # Rotate the array to its sorted position
                    rotated = A[drop_idx + 1:] + A[:drop_idx + 1]
                    if rotated != B:
                        return False
            return True

        ans = 0
        # Iterate over all possible divisors of n
        for k in range(1, n + 1):
            if n % k == 0:
                if check(k):
                    ans += k
        return ans

```

---

[View on LeetCode](https://leetcode.com/problems/sum-of-sortable-integers/)