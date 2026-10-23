class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Find all elements that are not in their sorted positions
        misplaced = [num for i, num in enumerate(nums) if num != i]
        
        # If the array is already sorted, return 0
        if not misplaced:
            return 0
        
        # Calculate the bitwise AND of all misplaced elements
        ans = misplaced[0]
        for num in misplaced[1:]:
            ans &= num
            
        return ans
