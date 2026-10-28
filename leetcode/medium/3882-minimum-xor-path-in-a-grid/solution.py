class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        # dp[j] stores the set of all achievable XOR values at column j for the current row
        dp = [set() for _ in range(n)]
        
        # Base case: Starting point (0, 0)
        dp[0].add(grid[0][0])
        
        # Initialize the first row (can only come from the left)
        for j in range(1, n):
            val = grid[0][j]
            dp[j] = {x ^ val for x in dp[j-1]}
            
        # Fill the rest of the DP table row by row
        for i in range(1, m):
            # First column of the current row (can only come from above)
            val = grid[i][0]
            dp[0] = {x ^ val for x in dp[0]}
            
            # Remaining columns (can come from above or from the left)
            for j in range(1, n):
                val = grid[i][j]
                combined_previous_states = dp[j] | dp[j-1]
                dp[j] = {x ^ val for x in combined_previous_states}
                
        # The answer is the minimum value in the final cell's set
        return min(dp[n-1])


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna