# Brace Expansion II

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Under the grammar given below, strings can represent a set of lowercase words. Let `R(expr)` denote the set of words the expression represents.

The grammar can best be understood through simple examples:

- Single letters represent a singleton set containing that word. R("a") = {"a"} R("w") = {"w"}
- When we take a comma-delimited list of two or more expressions, we take the union of possibilities. R("{a,b,c}") = {"a","b","c"} R("{{a,b},{b,c}}") = {"a","b","c"} (notice the final set only contains each word at most once)
- When we concatenate two expressions, we take the set of possible concatenations between two words where the first word comes from the first expression and the second word comes from the second expression. R("{a,b}{c,d}") = {"ac","ad","bc","bd"} R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"}

Formally, the three rules for our grammar:

- For every lowercase letter x, we have R(x) = {x}.
- For expressions e1, e2,..., ek with k >= 2, we have R({e1, e2,...}) = R(e1) ∪ R(e2) ∪...
- For expressions e1 and e2, we have R(e1 + e2) = {a + b for (a, b) in R(e1) × R(e2)}, where + denotes concatenation, and × denotes the cartesian product.

Given an expression representing a set of words under the given grammar, return  *the sorted list of words that the expression represents*.

 

 **Example 1:** 

```
Input: expression = "{a,b}{c,{d,e}}"
Output: ["ac","ad","ae","bc","bd","be"]

```

 **Example 2:** 

```
Input: expression = "{{a,z},a{b,c},{ab,z}}"
Output: ["a","ab","ac","z"]
Explanation: Each distinct word is written only once in the final answer.

```

 

 **Constraints:** 

- 1 <= expression.length <= 60
- expression[i] consists of '{', '}', ','or lowercase English letters.
- The given expression represents a set of words based on the grammar given in the description.

## Solution

**Language:** Python  
**Runtime:** 23 ms (beats 13.33%)  
**Memory:** 12.6 MB (beats 40.00%)  
**Submitted:** 2026-09-25T03:26:01.460Z  

```py
class Solution:
    def braceExpansionII(self, expression):
        s = {expression}
        while any('{' in x for x in s):
            next_s = set()
            for expr in s:
                i = 0
                while i < len(expr) and expr[i] != '}':
                    i += 1
                j = i
                while j >= 0 and expr[j] != '{':
                    j -= 1
                left = expr[:j]
                right = expr[i+1:]
                middle = expr[j+1:i].split(',')
                for m in middle:
                    next_s.add(left + m + right)
            s = next_s
        return sorted(list(s))

```

---

[View on LeetCode](https://leetcode.com/problems/brace-expansion-ii/)