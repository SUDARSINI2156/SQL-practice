class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        # If the required sum is impossible to achieve with `num` digits
        if sum > 9 * num:
            return ""
        
        # Calculate number of 9s and the remainder
        q = sum // 9
        r = sum % 9
        
        # Build the largest lexicographical number
        ans = "9" * q
        if r > 0:
            ans += str(r)
            
        # Pad the rest with 0s
        ans += "0" * (num - len(ans))
        
        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna