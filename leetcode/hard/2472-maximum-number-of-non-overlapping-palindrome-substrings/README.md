# Maximum Number of Non-overlapping Palindrome Substrings

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given a string `s` and a  **positive**  integer `k`.

Select a set of  **non-overlapping**  substrings from the string `s` that satisfy the following conditions:

- The length of each substring is at least k.
- Each substring is a palindrome.

Return  *the  **maximum**  number of substrings in an optimal selection*.

A  **substring**  is a contiguous sequence of characters within a string.

 

 **Example 1:** 

```
Input: s = "abaccdbbd", k = 3
Output: 2
Explanation: We can select the substrings underlined in s = "abaccdbbd". Both "aba" and "dbbd" are palindromes and have a length of at least k = 3.
It can be shown that we cannot find a selection with more than two valid substrings.

```

 **Example 2:** 

```
Input: s = "adbcda", k = 2
Output: 0
Explanation: There is no palindrome substring of length at least 2 in the string.

```

 

 **Constraints:** 

- 1 <= k <= s.length <= 2000
- s consists of lowercase English letters.

## Solution

**Language:** Java  
**Runtime:** 153 ms (beats 15.08%)  
**Memory:** 62.2 MB (beats 16.08%)  
**Submitted:** 2026-09-15T03:49:02.458Z  

```java
class Solution {
    public int maxPalindromes(String s, int k) {
        int n = s.length();

        // pal[i][j] = true if s[i...j] is a palindrome
        boolean[][] pal = new boolean[n][n];

        for (int len = 1; len <= n; len++) {
            for (int i = 0; i + len <= n; i++) {
                int j = i + len - 1;

                if (len == 1) {
                    pal[i][j] = true;
                } else if (len == 2) {
                    pal[i][j] = s.charAt(i) == s.charAt(j);
                } else {
                    pal[i][j] =
                        s.charAt(i) == s.charAt(j) &&
                        pal[i + 1][j - 1];
                }
            }
        }

        // dp[i] = maximum palindromes using s[0 ... i-1]
        int[] dp = new int[n + 1];

        for (int i = 0; i < n; i++) {
            // Skip s[i]
            dp[i + 1] = Math.max(dp[i + 1], dp[i]);

            // Try every palindrome ending at i
            for (int j = 0; j <= i; j++) {
                int len = i - j + 1;

                if (len >= k && pal[j][i]) {
                    dp[i + 1] = Math.max(
                        dp[i + 1],
                        dp[j] + 1
                    );
                }
            }
        }

        return dp[n];
    }
}
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/)