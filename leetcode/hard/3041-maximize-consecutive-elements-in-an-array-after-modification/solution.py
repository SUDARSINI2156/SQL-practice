class Solution(object):
    def maxSelectedElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        dp = {}
        ans = 0
        
        for x in nums:
            # Option 1: Increment x to x + 1 (extends sequence ending at x)
            dp[x + 1] = dp.get(x, 0) + 1
            
            # Option 2: Keep x as is (extends sequence ending at x - 1)
            dp[x] = dp.get(x - 1, 0) + 1
            
            ans = max(ans, dp[x], dp[x + 1])
            
        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna