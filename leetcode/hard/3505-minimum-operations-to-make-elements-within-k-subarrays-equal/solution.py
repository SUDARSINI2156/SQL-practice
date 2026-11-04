
from sortedcontainers import SortedList

class Solution(object):
    def minOperations(self, nums, x, k):
        """
        :type nums: List[int]
        :type x: int
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if k * x > n:
            return -1
        
        left = SortedList()
        right = SortedList()
        
        # Using a list to hold mutable state integers to bypass Python 2 scoping limits
        sums = [0, 0] # [left_sum, right_sum]
        left_size = x // 2
        
        # 1. Precompute costs for all possible windows of size x
        C = []
        for i in range(n):
            # Inline Add logic
            item = (nums[i], i)
            val = item[0]
            if not left or item <= left[-1]:
                left.add(item)
                sums[0] += val
            else:
                right.add(item)
                sums[1] += val
                
            if i >= x:
                # Inline Remove logic
                rem_item = (nums[i - x], i - x)
                rem_val = rem_item[0]
                if rem_item in left:
                    left.remove(rem_item)
                    sums[0] -= rem_val
                else:
                    right.remove(rem_item)
                    sums[1] -= rem_val
            
            # Inline Balance logic
            while len(left) > left_size:
                pop_item = left.pop(-1)
                sums[0] -= pop_item[0]
                right.add(pop_item)
                sums[1] += pop_item[0]
            while len(left) < left_size and right:
                pop_item = right.pop(0)
                sums[1] -= pop_item[0]
                left.add(pop_item)
                sums[0] += pop_item[0]
                
            if i >= x - 1:
                med = right[0][0]
                cost = (sums[1] - len(right) * med) + (len(left) * med - sums[0])
                C.append(cost)
                
        # 2. Dynamic Programming to find the optimal k choices
        dp = [0] * (n + 1)
        
        for _ in range(k):
            next_dp = [float('inf')] * (n + 1)
            for j in range(x, n + 1):
                next_dp[j] = next_dp[j - 1]
                if dp[j - x] != float('inf'):
                    next_dp[j] = min(next_dp[j], dp[j - x] + C[j - x])
            dp = next_dp
                    
        return dp[n]
