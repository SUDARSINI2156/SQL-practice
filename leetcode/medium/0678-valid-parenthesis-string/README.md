# Valid Parenthesis String

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string `s` containing only three types of characters: `'('`, `')'` and `' *'`, return `true`* if *`s`* is  **valid** *.

The following rules define a  **valid**  string:

- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
- Any right parenthesis ')' must have a corresponding left parenthesis '('.
- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
- '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

 

 **Example 1:** 

```
Input: s = "()"
Output: true

```

 **Example 2:** 

```
Input: s = "(*)"
Output: true

```

 **Example 3:** 

```
Input: s = "(*))"
Output: true

```

 **Example 4:** 

```
Input: s = "("
Output: false

```

 

 **Constraints:** 

- 1 <= s.length <= 100
- s[i] is '(', ')' or '*'.

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 12.3 MB (beats 92.02%)  
**Submitted:** 2026-10-04T06:39:31.916Z  

```py
class Solution(object):
    def checkValidString(self, s):
        cmin = 0  # Jumlah minimum '(' yang harus ditutup
        cmax = 0  # Jumlah maksimum '(' yang bisa ditutup
        
        for char in s:
            if char == '(':
                cmin += 1
                cmax += 1
            elif char == ')':
                cmin -= 1
                cmax -= 1
            elif char == '*':
                cmin -= 1  # '*' dianggap sebagai ')'
                cmax += 1  # '*' dianggap sebagai '('
            
            if cmax < 0:
                return False
            
            cmin = max(cmin, 0)
            
        return cmin == 0

```

---

[View on LeetCode](https://leetcode.com/problems/valid-parenthesis-string/)