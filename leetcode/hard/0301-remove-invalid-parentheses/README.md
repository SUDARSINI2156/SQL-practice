# Remove Invalid Parentheses

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given a string `s` that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return  *a list of  **unique strings**  that are valid with the minimum number of removals*. You may return the answer in  **any order**.

 

 **Example 1:** 

```
Input: s = "()())()"
Output: ["(())()","()()()"]

```

 **Example 2:** 

```
Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

```

 **Example 3:** 

```
Input: s = ")("
Output: [""]

```

 

 **Constraints:** 

- 1 <= s.length <= 25
- s consists of lowercase English letters and parentheses '(' and ')'.
- There will be at most 20 parentheses in s.

## Solution

**Language:** Python  
**Runtime:** 100 ms (beats 84.88%)  
**Memory:** 12.6 MB (beats 75.93%)  
**Submitted:** 2026-10-07T05:38:57.102Z  

```py
class Solution:
    def removeInvalidParentheses(self, s):
        def isValid(x):
            count = 0

            for ch in x:
                if ch == '(':
                    count += 1

                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        current = {s}

        while True:
            answer = []

            # Check current strings
            for x in current:
                if isValid(x):
                    answer.append(x)

            # If valid strings found,
            # this is the minimum number of removals
            if answer:
                return answer

            next_level = set()

            # Remove one parenthesis
            for x in current:
                for i in range(len(x)):
                    if x[i] == '(' or x[i] == ')':
                        new_string = x[:i] + x[i + 1:]
                        next_level.add(new_string)

            current = next_level
```

---

[View on LeetCode](https://leetcode.com/problems/remove-invalid-parentheses/)