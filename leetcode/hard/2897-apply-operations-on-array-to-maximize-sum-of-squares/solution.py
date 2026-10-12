class Solution(object):
    def maxSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # Step 1: Count the total frequency of 1s at each bit position
        bit_counts = [0] * 32
        for num in nums:
            for i in range(32):
                if (num >> i) & 1:
                    bit_counts[i] += 1
                    
        # Step 2: Greedily reconstruct the k largest possible numbers
        ans = 0
        for _ in range(k):
            current_num = 0
            for i in range(32):
                if bit_counts[i] > 0:
                    current_num |= (1 << i)
                    bit_counts[i] -= 1
            
            # Step 3: Add the square of the reconstructed number to the answer
            ans = (ans + current_num * current_num) % MOD
            
        return ans
