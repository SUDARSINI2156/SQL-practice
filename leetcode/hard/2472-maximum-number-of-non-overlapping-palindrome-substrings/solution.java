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