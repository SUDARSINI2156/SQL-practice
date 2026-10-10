class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        k = k1 + k2
        
        diffs = [abs(n1 - n2) for n1, n2 in zip(nums1, nums2)]
        total_diff = sum(diffs)
        
        if total_diff <= k:
            return 0
        
        max_diff = max(diffs)
        buckets = [0] * (max_diff + 1)
        
        for d in diffs:
            buckets[d] += 1
            
        for d in range(max_diff, 0, -1):
            if buckets[d] == 0:
                continue
                
            count = buckets[d]
            ops_to_use = min(k, count)
            
            buckets[d] -= ops_to_use
            buckets[d - 1] += ops_to_use
            
            k -= ops_to_use
            if k == 0:
                break
                
        return sum(count * (d ** 2) for d, count in enumerate(buckets) if count > 0)
