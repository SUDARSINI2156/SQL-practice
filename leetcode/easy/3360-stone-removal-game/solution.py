class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        stones_to_remove = 10
        turns = 0
        
        while n >= stones_to_remove and stones_to_remove > 0:
            n -= stones_to_remove
            stones_to_remove -= 1
            turns += 1
            
        return turns % 2 == 1
