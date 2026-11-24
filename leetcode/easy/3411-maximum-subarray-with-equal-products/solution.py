from fractions import gcd

class Solution(object):
    def maxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def lcm(a, b):
            return (a * b) // gcd(a, b)

        n = len(nums)
        ans = 0
        
        # Compute upper bound for any valid subarray product
        total_lcm = 1
        for x in nums:
            total_lcm = lcm(total_lcm, x)
        max_p = total_lcm * max(nums)

        for i in range(n):
            p, g, l = 1, 0, 1
            for j in range(i, n):
                p *= nums[j]
                g = gcd(g, nums[j])
                l = lcm(l, nums[j])
                
                if p == g * l:
                    ans = max(ans, j - i + 1)
                if p > max_p:
                    break
                    
        return ans
