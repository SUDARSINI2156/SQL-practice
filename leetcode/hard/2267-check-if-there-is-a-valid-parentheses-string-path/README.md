# Check if There Is a Valid Parentheses String Path

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

A parentheses string is a  **non-empty**  string consisting only of `'('` and `')'`. It is  **valid**  if  **any**  of the following conditions is  **true** :

- It is ().
- It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
- It can be written as (A), where A is a valid parentheses string.

You are given an `m x n` matrix of parentheses `grid`. A  **valid parentheses string path**  in the grid is a path satisfying  **all**  of the following conditions:

- The path starts from the upper left cell (0, 0).
- The path ends at the bottom-right cell (m - 1, n - 1).
- The path only ever moves down or right.
- The resulting parentheses string formed by the path is valid.

Return `true`  *if there exists a  **valid parentheses string path**  in the grid.*  Otherwise, return `false`.

 

 **Example 1:** 

```
Input: grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
Output: true
Explanation: The above diagram shows two possible paths that form valid parentheses strings.
The first path shown results in the valid parentheses string "()(())".
The second path shown results in the valid parentheses string "((()))".
Note that there may be other valid parentheses string paths.

```

 **Example 2:** 

```
Input: grid = [[")",")"],["(","("]]
Output: false
Explanation: The two possible paths form the parentheses strings "))(" and ")((". Since neither of them are valid parentheses strings, we return false.

```

 

 **Constraints:** 

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 100
- grid[i][j] is either '(' or ')'.

## Solution

**Language:** Python  
**Runtime:** 21 ms (beats 76.92%)  
**Memory:** 18.2 MB (beats 76.92%)  
**Submitted:** 2026-09-29T05:26:33.522Z  

```py
class Solution(object):
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        
        # Jika panjang total jalur ganjil, tidak mungkin membentuk kurung valid
        if (m + n - 1) % 2 != 0:
            return False
            
        # Jika sel awal adalah ')' atau sel akhir adalah '(', jalur tidak valid
        if grid[0][0] == ")" or grid[m - 1][n - 1] == "(":
            return False
            
        memo = set()
        
        def dfs(r, c, balance):
            # Perbarui balance berdasarkan karakter saat ini
            if grid[r][c] == "(":
                balance += 1
            else:
                balance -= 1
                
            # Jika kelebihan ')', jalur langsung tidak valid
            if balance < 0:
                return False
                
            # Jika sampai di ujung bawah-kanan
            if r == m - 1 and c == n - 1:
                return balance == 0
                
            # Cek memo untuk menghindari pengerjaan ulang
            if (r, c, balance) in memo:
                return False
            memo.add((r, c, balance))
            
            # Bergerak ke bawah atau ke kanan
            if r + 1 < m and dfs(r + 1, c, balance):
                return True
            if c + 1 < n and dfs(r, c + 1, balance):
                return True
                
            return False
            
        return dfs(0, 0, 0)

```

---

[View on LeetCode](https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/)