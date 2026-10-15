class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = 0
        n = len(nums)
        
        # i represents the starting point of the subarray
        for i in range(n):
            distinct_set = set()
            
            # j represents the ending point of the subarray
            for j in range(i, n):
                distinct_set.add(nums[j])
                
                # Get the count of distinct elements
                distinct_count = len(distinct_set)
                
                # Add the square of the distinct count to the total sum
                total_sum += distinct_count * distinct_count
                
        return total_sum
