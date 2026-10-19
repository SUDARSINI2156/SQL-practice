class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        less_than = 0
        equal_to = 0
        
        for num in nums:
            if num < target:
                less_than += 1
            elif num == target:
                equal_to += 1
                
        # Generate the sorted target indices
        return [i for i in range(less_than, less_than + equal_to)]
