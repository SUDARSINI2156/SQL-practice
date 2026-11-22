# Check if All A's Appears Before All B's

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string `s` consisting of  **only**  the characters `'a'` and `'b'`, return `true`  *if  **every*** `'a'`  *appears before  **every*** `'b'` *in the string*. Otherwise, return `false`.

 

Original
Python
 **Example 1:** 

```
Input: s = "aaabbb"
Output: true
Explanation:
The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
Hence, every 'a' appears before every 'b' and we return true.

```

 **Example 2:** 

```
Input: s = "abab"
Output: false
Explanation:
There is an 'a' at index 2 and a 'b' at index 1.
Hence, not every 'a' appears before every 'b' and we return false.

```

 **Example 3:** 

```
Input: s = "bbb"
Output: true
Explanation:
There are no 'a's, hence, every 'a' appears before every 'b' and we return true.

```

 

 **Constraints:** 

- 1 <= s.length <= 100
- s[i] is either 'a' or 'b'.

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 12.3 MB (beats 35.93%)  
**Submitted:** 2026-11-22T07:22:39.872Z  

```py
class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return "ba" not in s

```

---

[View on LeetCode](https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/)