class Solution(object):
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        # Track the minimum costs for steps: j-3, j-2, and j-1
        # Initially, step 0 has cost 0, and out-of-bounds steps are infinity
        prev3 = float('inf')  # Represents dp[j - 3]
        prev2 = float('inf')  # Represents dp[j - 2]
        prev1 = 0             # Represents dp[0]
        
        for j in range(1, n + 1):
            # Calculate the minimum cost to jump to step j from valid prior steps
            jump1 = prev1 + 1
            jump2 = prev2 + 4
            jump3 = prev3 + 9
            
            # costs is 0-indexed in Python, so step j corresponds to costs[j - 1]
            curr = costs[j - 1] + min(jump1, jump2, jump3)
            
            # Shift the rolling variables forward for the next step
            prev3, prev2, prev1 = prev2, prev1, curr
            
        return prev1
