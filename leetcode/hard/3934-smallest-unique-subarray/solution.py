from collections import Counter

class Solution(object):
    def smallestUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # Double hashing constants to virtually eliminate hash collisions
        BASE1, MOD1 = 1315423911, 10**9 + 7
        BASE2, MOD2 = 2654435761, 10**9 + 9
        
        # Shift values by +1 in case nums contains 0 or negative numbers
        # (Alternatively, map numbers to positive ranks if negatives exist)
        min_val = min(nums)
        arr = [x - min_val + 1 for x in nums]

        def has_unique_subarray(length):
            h1 = h2 = 0
            p1 = pow(BASE1, length - 1, MOD1)
            p2 = pow(BASE2, length - 1, MOD2)
            
            # Build hash for the first window of size `length`
            for i in range(length):
                h1 = (h1 * BASE1 + arr[i]) % MOD1
                h2 = (h2 * BASE2 + arr[i]) % MOD2
                
            counts = Counter([(h1, h2)])
            
            # Slide the window across the rest of the array in O(1) per step
            for i in range(length, n):
                # Remove leftmost element
                h1 = (h1 - arr[i - length] * p1) % MOD1
                h2 = (h2 - arr[i - length] * p2) % MOD2
                
                # Shift and add new rightmost element
                h1 = (h1 * BASE1 + arr[i]) % MOD1
                h2 = (h2 * BASE2 + arr[i]) % MOD2
                
                counts[(h1, h2)] += 1
                
            return 1 in counts.values()

        # Binary search for the smallest valid length
        left, right = 1, n
        ans = n
        while left <= right:
            mid = (left + right) // 2
            if has_unique_subarray(mid):
                ans = mid
                right = mid - 1  # Try to find an even smaller length
            else:
                left = mid + 1   # Need a longer subarray to make it unique
                
        return ans
