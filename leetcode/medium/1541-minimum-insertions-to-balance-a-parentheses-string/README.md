# Minimum Insertions to Balance a Parentheses String

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a parentheses string `s` containing only the characters `'('` and `')'`. A parentheses string is  **balanced**  if:

- Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
- Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.

In other words, we treat `'('` as an opening parenthesis and `'))'` as a closing parenthesis.

- For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.

You can insert the characters `'('` and `')'` at any position of the string to balance it if needed.

Return  *the minimum number of insertions*  needed to make `s` balanced.

 

 **Example 1:** 

```
Input: s = "(()))"
Output: 1
Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to add one more ')' at the end of the string to be "(())))" which is balanced.

```

 **Example 2:** 

```
Input: s = "())"
Output: 0
Explanation: The string is already balanced.

```

 **Example 3:** 

```
Input: s = "))())("
Output: 3
Explanation: Add '(' to match the first '))', Add '))' to match the last '('.

```

 

 **Constraints:** 

- 1 <= s.length <= 105
- s consists of '(' and ')' only.

## Solution

**Language:** Python  
**Runtime:** 85 ms (beats 84.78%)  
**Memory:** 12.9 MB (beats 30.43%)  
**Submitted:** 2026-10-09T05:35:11.659Z  

```py
class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        needed_right = 0   # Tracks how many ')' are currently needed
        insertions = 0     # Tracks total additions of '(' or ')'
        
        for char in s:
            if char == '(':
                # If we encounter an open '(' but currently need an odd number of ')',
                # it means the previous '(' only has one ')'. We must insert a ')' 
                # immediately to close it properly before starting a new group.
                if needed_right % 2 == 1:
                    insertions += 1
                    needed_right -= 1
                needed_right += 2
            else:
                # Character is ')'
                needed_right -= 1
                # If needed_right drops below 0, we have an unmatched ')' sequence.
                # We balance it by inserting an open '(' (which grants 2 ')' credits).
                if needed_right < 0:
                    insertions += 1
                    needed_right += 2
                    
        # Any remaining needed_right counts must be handled by adding closing brackets
        return insertions + needed_right

```

---

[View on LeetCode](https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/)