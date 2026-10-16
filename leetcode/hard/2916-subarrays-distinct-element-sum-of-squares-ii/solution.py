class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        MOD = 10**9 + 7
        
        # Segment tree arrays (size 4 * n)
        # sum_sq stores the sum of squares of distinct counts
        # sum_val stores the sum of distinct counts (needed for expanding (x+1)^2 = x^2 + 2x + 1)
        sum_sq = [0] * (4 * n)
        sum_val = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def push(node, start, end):
            if lazy[node] == 0:
                return
            
            lazy_val = lazy[node]
            mid = (start + end) // 2
            
            # Left child update
            left_len = mid - start + 1
            sum_sq[2 * node] = (sum_sq[2 * node] + 2 * lazy_val * sum_val[2 * node] + lazy_val * lazy_val * left_len) % MOD
            sum_val[2 * node] = (sum_val[2 * node] + lazy_val * left_len) % MOD
            lazy[2 * node] += lazy_val
            
            # Right child update
            right_len = end - mid
            sum_sq[2 * node + 1] = (sum_sq[2 * node + 1] + 2 * lazy_val * sum_val[2 * node + 1] + lazy_val * lazy_val * right_len) % MOD
            sum_val[2 * node + 1] = (sum_val[2 * node + 1] + lazy_val * right_len) % MOD
            lazy[2 * node + 1] += lazy_val
            
            lazy[node] = 0

        def update(node, start, end, l, r, val):
            if r < start or end < l:
                return
            if l <= start and end <= r:
                length = end - start + 1
                sum_sq[node] = (sum_sq[node] + 2 * val * sum_val[node] + val * val * length) % MOD
                sum_val[node] = (sum_val[node] + val * length) % MOD
                lazy[node] += val
                return
                
            push(node, start, end)
            mid = (start + end) // 2
            update(2 * node, start, mid, l, r, val)
            update(2 * node + 1, mid + 1, end, l, r, val)
            
            sum_sq[node] = (sum_sq[2 * node] + sum_sq[2 * node + 1]) % MOD
            sum_val[node] = (sum_val[2 * node] + sum_val[2 * node + 1]) % MOD

        total_sum = 0
        last_pos = {}
        
        for j in range(n):
            # Find the last occurrence of the current element
            prev_idx = last_pos.get(nums[j], -1)
            
            # Increment distinct counts for all valid left endpoints in range [prev_idx + 1, j]
            update(1, 0, n - 1, prev_idx + 1, j, 1)
            
            # The root node (index 1) maintains the total sum of squares for all subarrays ending at index j
            total_sum = (total_sum + sum_sq[1]) % MOD
            
            # Update the latest seen position of this element
            last_pos[nums[j]] = j
            
        return total_sum


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna