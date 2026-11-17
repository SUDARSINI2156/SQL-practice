class Solution(object):
    def minimumChanges(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        
        # Precompute proper divisors for all possible lengths 1..n
        divisors = [[] for _ in range(n + 1)]
        for length in range(2, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divisors[length].append(d)
                    
        # Precompute cost[i][j]: min changes to make s[i..j] a semi-palindrome
        INF = float('inf')
        cost = [[INF] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                min_changes = INF
                
                for d in divisors[length]:
                    changes = 0
                    # Check each of the d interleaved groups
                    for rem in range(d):
                        left = i + rem
                        right = j - (d - 1 - rem)
                        while left < right:
                            if s[left] != s[right]:
                                changes += 1
                            left += d
                            right -= d
                    min_changes = min(min_changes, changes)
                    
                cost[i][j] = min_changes
                
        # DP to partition s[0..i-1] into p semi-palindromes
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        
        for p in range(1, k + 1):
            # Need at least 2*p characters to form p semi-palindromes
            for i in range(2 * p, n + 1):
                # Split point prev must leave at least 2*(p-1) chars on the left
                # and at least 2 chars on the right (prev <= i - 2)
                for prev in range(2 * (p - 1), i - 1):
                    if dp[prev][p - 1] != INF:
                        dp[i][p] = min(dp[i][p], dp[prev][p - 1] + cost[prev][i - 1])
                        
        return dp[n][k]
