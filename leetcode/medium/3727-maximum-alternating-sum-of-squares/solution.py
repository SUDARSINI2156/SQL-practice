class Solution(object):
    def maxAlternatingSum(self, nums):
       
        squares = sorted(x * x for x in nums)
        
      
        num_negatives = len(nums) // 2
        
       
        return sum(squares[num_negatives:]) - sum(squares[:num_negatives])
