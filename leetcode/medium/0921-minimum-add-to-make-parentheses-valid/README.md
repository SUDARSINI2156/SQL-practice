# Minimum Add to Make Parentheses Valid

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

A parentheses string is valid if and only if:

- It is the empty string,
- It can be written as AB (A concatenated with B), where A and B are valid strings, or
- It can be written as (A), where A is a valid string.

You are given a parentheses string `s`. In one move, you can insert a parenthesis at any position of the string.

- For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".

Return  *the minimum number of moves required to make* `s` *valid*.

 

 **Example 1:** 

```
Input: s = "())"
Output: 1

```

 **Example 2:** 

```
Input: s = "((("
Output: 3

```

 

 **Constraints:** 

- 1 <= s.length <= 1000
- s[i] is either '(' or ')'.

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 12.2 MB (beats 99.56%)  
**Submitted:** 2026-10-06T07:16:04.990Z  

```py
class Solution(object):
    def minAddToMakeValid(self, s):
        buka = 0
        tambah = 0
        
        for char in s:
            if char == '(':
                buka += 1
            else:  # char == ')'
                if buka > 0:
                    buka -= 1
                else:
                    tambah += 1
                    
        return tambah + buka

```

---

[View on LeetCode](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)