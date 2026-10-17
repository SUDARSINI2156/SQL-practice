class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get_digit_sum(n):
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s
        
        # 1. Pair each number with its original index and sort by custom criteria
        # Priority 1: Digit sum (increasing)
        # Priority 2: Actual value (increasing)
        indexed_nums = [(num, idx) for idx, num in enumerate(nums)]
        indexed_nums.sort(key=lambda x: (get_digit_sum(x[0]), x[0]))
        
        # 2. Track visited positions to find graph cycles
        n = len(nums)
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            # If already visited or already in the correct position, skip
            if visited[i] or indexed_nums[i][1] == i:
                continue
                
            # Calculate the size of the current cycle
            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                # Move to the original index of the element currently occupying this position
                curr = indexed_nums[curr][1]
                cycle_size += 1
                
            # If cycle_size > 0, it contributes (cycle_size - 1) swaps
            if cycle_size > 0:
                swaps += (cycle_size - 1)
                
        return swaps
