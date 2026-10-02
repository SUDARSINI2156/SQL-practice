# Generate Parentheses

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given `n` pairs of parentheses, write a function to  *generate all combinations of well-formed parentheses*.

 

 **Example 1:** 

```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

```

 **Example 2:** 

```
Input: n = 1
Output: ["()"]

```

 

 **Constraints:** 

- 1 <= n <= 8

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 12.7 MB (beats 20.61%)  
**Submitted:** 2026-10-02T16:15:13.904Z  

```py
class Solution(object):
    def generateParenthesis(self, n):
        result = []
        
        def backtrack(current_str, open_count, close_count):
            # Jika panjang string sudah mencapai 2 * n, kombinasi selesai
            if len(current_str) == 2 * n:
                result.append(current_str)
                return
            
            # Tambahkan kurung buka jika jumlahnya belum mencapai n
            if open_count < n:
                backtrack(current_str + "(", open_count + 1, close_count)
                
            # Tambahkan kurung tutup jika jumlahnya lebih sedikit dari kurung buka
            if close_count < open_count:
                backtrack(current_str + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result

```

---

[View on LeetCode](https://leetcode.com/problems/generate-parentheses/)