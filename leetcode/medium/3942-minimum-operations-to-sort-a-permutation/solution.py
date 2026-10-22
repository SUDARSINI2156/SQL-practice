class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        zero = nums.index(0)
        
        # Helper to verify if the cyclic permutation matches the expected direction
        def check(step):
            for i in range(n):
                if nums[(zero + i * step) % n] != i:
                    return False
            return True

        ans = float('inf')
        
        # Case 1: Increasing cyclic order
        if check(1):
            ans = min(ans, zero)          # Direct left rotations
            ans = min(ans, n - zero + 2)  # Reverse -> Rotate -> Reverse
            
        # Case 2: Decreasing cyclic order
        if check(-1):
            ans = min(ans, zero + 2)      # Rotate -> Reverse
            ans = min(ans, n - zero)      # Reverse -> Rotate
            
        return ans if ans != float('inf') else -1
