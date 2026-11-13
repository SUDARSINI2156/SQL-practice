from collections import deque

class Solution(object):
    def countNonDecreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        ans = 0
        cost = 0
        r = n - 1
        # Monotonic decreasing deque storing pairs of [value, count]
        q = deque()
        
        for l in range(n - 1, -1, -1):
            curr = nums[l]
            count = 1
            
            # Merge all elements to the right that are smaller than nums[l]
            while q and q[0][0] < curr:
                val, cnt = q.popleft()
                # Increasing these `cnt` elements from `val` to `curr` adds cost
                cost += (curr - val) * cnt
                count += cnt
                
            q.appendleft([curr, count])
            
            # Shrink the window from the right while operations exceed k
            while cost > k:
                # Subtract the cost contribution of the rightmost element
                cost -= q[-1][0] - nums[r]
                q[-1][1] -= 1
                if q[-1][1] == 0:
                    q.pop()
                r -= 1
                
            # All subarrays starting at l and ending between l and r are valid
            ans += r - l + 1
            
        return ans
