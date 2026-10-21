# Minimum Operations to Sort a String

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a string `s` consisting of lowercase English letters.

In one operation, you can select any  **substring**  of `s` that is  **not**  the entire string and  **sort**  it in  **non-descending alphabetical**  order.

Return the  **minimum**  number of operations required to make `s` sorted in  **non-descending**  order. If it is not possible, return -1.

 

 **Example 1:** 

 **Input:**  s = "dog"

 **Output:**  1

 **Explanation:** ​​​​​​​

- Sort substring "og" to "go".
- Now, s = "dgo", which is sorted in ascending order. Thus, the answer is 1.

 **Example 2:** 

 **Input:**  s = "card"

 **Output:**  2

 **Explanation:** 

- Sort substring "car" to "acr", so s = "acrd".
- Sort substring "rd" to "dr", making s = "acdr", which is sorted in ascending order. Thus, the answer is 2.

 **Example 3:** 

 **Input:**  s = "gf"

 **Output:**  -1

 **Explanation:** 

- It is impossible to sort s under the given constraints. Thus, the answer is -1.

 

 **Constraints:** 

- 1 <= s.length <= 105
- s consists of only lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 388 ms (beats 36.36%)  
**Memory:** 14.1 MB (beats 90.91%)  
**Submitted:** 2026-10-21T04:13:14.583Z  

```py

class Solution:
    def minOperations(self, s):
        n = len(s)
        sorted_s = ''.join(sorted(s))

        if s == sorted_s:
            return 0

        if n == 2:
            return -1

        smallest = min(s)
        largest = max(s)

        if s[0] == smallest or s[-1] == largest:
            return 1

        if s[0] == largest and s[-1] == smallest:
            if s.count(largest) == 1 and s.count(smallest) == 1:
                return 3

        return 2

```

---

[View on LeetCode](https://leetcode.com/problems/minimum-operations-to-sort-a-string/)