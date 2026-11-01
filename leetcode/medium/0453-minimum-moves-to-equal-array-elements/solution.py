class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # The sum of differences between each element and the minimum element
        return sum(nums) - len(nums) * min(nums)
