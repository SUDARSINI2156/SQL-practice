class Solution(object):
    def sortableIntegers(self, nums):
        """
        :type nums: List[int]
        :type : rtype: int
        """
        n = len(nums)
        S = sorted(nums)
        
        def check(k):
            for i in range(0, n, k):
                A = nums[i:i+k]
                B = S[i:i+k]
                
                drops = 0
                drop_idx = -1
                
                # Count drops with wrap-around
                for j in range(k):
                    if A[j] > A[(j + 1) % k]:
                        drops += 1
                        drop_idx = j
                        if drops > 1:
                            return False
                
                if drops == 0:
                    if A != B:
                        return False
                else:
                    # Rotate the array to its sorted position
                    rotated = A[drop_idx + 1:] + A[:drop_idx + 1]
                    if rotated != B:
                        return False
            return True

        ans = 0
        # Iterate over all possible divisors of n
        for k in range(1, n + 1):
            if n % k == 0:
                if check(k):
                    ans += k
        return ans
