class Solution(object):
    def maximumSaleItems(self, items, budget):
        """
        :type items: List[List[int]]
        :type budget: int
        :rtype: int
        """
        n = len(items)
        
        # 1. Precompute free items gained from buying the first copy of item i
        free_counts = [0] * n
        for i in range(n):
            fac_i = items[i][0]
            for j in range(n):
                if i != j and items[j][0] % fac_i == 0:
                    free_counts[i] += 1
                    
        # 2. 0-1 Knapsack for the first purchase of each item
        # dp[c] = max items obtained using exact cost c from first-time purchases
        dp = [-1] * (budget + 1)
        dp[0] = 0
        
        for i in range(n):
            cost = items[i][1]
            gain = 1 + free_counts[i]
            # Iterate backwards for 0-1 knapsack
            for c in range(budget, cost - 1, -1):
                if dp[c - cost] != -1:
                    dp[c] = max(dp[c], dp[c - cost] + gain)
                    
        # 3. Spend any remaining budget on the cheapest available item
        min_price = min(price for _, price in items)
        ans = 0
        for c in range(budget + 1):
            if dp[c] != -1:
                extra_copies = (budget - c) // min_price
                ans = max(ans, dp[c] + extra_copies)
                
        return ans
