class Solution(object):
    def minimizeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        # Option 1: Change the two smallest elements
        change_two_smallest = nums[-1] - nums[2]
        
        # Option 2: Change the two largest elements
        change_two_largest = nums[-3] - nums[0]
        
        # Option 3: Change one smallest and one largest element
        change_both_ends = nums[-2] - nums[1]
        
        return min(change_two_smallest, change_two_largest, change_both_ends)
