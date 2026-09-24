# Smallest Index With Digit Sum Equal to Index

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given an integer array `nums`.

Return the  **smallest**  index `i` such that the sum of the digits of `nums[i]` is equal to `i`.

If no such index exists, return `-1`.

 

 **Example 1:** 

 **Input:**  nums = [1,3,2]

 **Output:**  2

 **Explanation:** 

- For nums[2] = 2, the sum of digits is 2, which is equal to index i = 2. Thus, the output is 2.

 **Example 2:** 

 **Input:**  nums = [1,10,11]

 **Output:**  1

 **Explanation:** 

- For nums[1] = 10, the sum of digits is 1 + 0 = 1, which is equal to index i = 1.
- For nums[2] = 11, the sum of digits is 1 + 1 = 2, which is equal to index i = 2.
- Since index 1 is the smallest, the output is 1.

 **Example 3:** 

 **Input:**  nums = [1,2,3]

 **Output:**  -1

 **Explanation:** 

- Since no index satisfies the condition, the output is -1.

 

 **Constraints:** 

- 1 <= nums.length <= 100
- 0 <= nums[i] <= 1000

## Solution

**Language:** Java  
**Runtime:** 1 ms (beats 99.69%)  
**Memory:** 45.7 MB (beats 24.38%)  
**Submitted:** 2026-09-24T06:36:52.976Z  

```java
class Solution {
    public int smallestIndex(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            if (getDigitSum(nums[i]) == i) {
                return i; // Karena bergerak dari 0, ini pasti indeks terkecil
            }
        }
        return -1; // Jika tidak ada indeks yang memenuhi syarat
    }

    // Fungsi pembantu untuk menghitung jumlah digit secara matematis
    private int getDigitSum(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}

```

---

[View on LeetCode](https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/)