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
**Runtime:** 0 ms  
**Memory:** 12.1 MB  
**Submitted:** 2026-10-21T04:07:17.127Z  

```py
class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        sorted_s = "".join(sorted(s))
        
        # Case 0: String is already sorted
        if s == sorted_s:
            return 0
            
        n = len(s)
        
        # Case 1: A boundary character is already in its correct final home.
        if s[0] == sorted_s[0] or s[n-1] == sorted_s[n-1]:
            return 1
            
        # Case 2: The absolute max is at the front and absolute min is at the back
        if s[0] == sorted_s[n-1] and s[n-1] == sorted_s[0]:
            
            # Check if the middle section contains only a uniform repeating character
            # (or is empty, which handles n=2 and n=3 automatically)
            middle_section = s[1:n-1]
            if len(set(middle_section)) <= 1:
                if n == 2:
                    return -1 # "gf" -> Completely impossible
                else:
                    return 3  # "edc", "srrp" -> Requires 3 rolling operations
                
        # Case 3: All other mixed configurations can be solved in 2 steps
        return 2

```

---

[View on LeetCode](https://leetcode.com/problems/minimum-operations-to-sort-a-string/)