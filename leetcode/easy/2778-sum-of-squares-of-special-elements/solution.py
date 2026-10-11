class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_sum = 0
        
        # Loop through 1-indexed positions
        for i in range(1, n + 1):
            # Check if i divides n perfectly
            if n % i == 0:
                # Map 1-based index 'i' to 0-based index 'i - 1'
                total_sum += nums[i - 1] * nums[i - 1]
                
        return total_sum
