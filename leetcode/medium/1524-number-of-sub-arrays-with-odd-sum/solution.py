class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        
        odd_count = 0
        even_count = 1  # Empty prefix sum (0) is even
        prefix_sum = 0
        result = 0
        
        for num in arr:
            prefix_sum += num
            
            if prefix_sum % 2 == 1:
                # Odd prefix sum pairs with all previous even prefix sums
                result = (result + even_count) % MOD
                odd_count += 1
            else:
                # Even prefix sum pairs with all previous odd prefix sums
                result = (result + odd_count) % MOD
                even_count += 1
                
        return result
