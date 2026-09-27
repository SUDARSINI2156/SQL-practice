# Reverse Substrings Between Each Pair of Parentheses

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a string `s` that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should  **not**  contain any brackets.

 

 **Example 1:** 

```
Input: s = "(abcd)"
Output: "dcba"

```

 **Example 2:** 

```
Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.

```

 **Example 3:** 

```
Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.

```

 

 **Constraints:** 

- 1 <= s.length <= 2000
- s only contains lower case English characters and parentheses.
- It is guaranteed that all parentheses are balanced.

## Solution

**Language:** Python  
**Runtime:** 34 ms (beats 24.00%)  
**Memory:** 12.5 MB (beats 49.33%)  
**Submitted:** 2026-09-27T13:58:03.727Z  

```py
class Solution(object):
    def reverseParentheses(self, s):
        stack = []
        
        for char in s:
            if char == ')':
                portion = []
                while stack and stack[-1] != '(':
                    portion.append(stack.pop())
                
                if stack:
                    stack.pop()  # Hapus '('
                
                stack.extend(portion)
            else:
                stack.append(char)
                
        return "".join(stack)

```

---

[View on LeetCode](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/)