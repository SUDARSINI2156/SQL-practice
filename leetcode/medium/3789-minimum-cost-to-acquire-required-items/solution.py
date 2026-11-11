class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        """
        :type cost1: int
        :type cost2: int
        :type costBoth: int
        :type need1: int
        :type need2: int
        :rtype: int
        """
        # Best cost to cover 1 unit of both requirements simultaneously
        pair_cost = min(costBoth, cost1 + cost2)
        
        # Best cost to cover a single remaining unit (over-buying is allowed if cheaper)
        single1_cost = min(cost1, costBoth)
        single2_cost = min(cost2, costBoth)
        
        common = min(need1, need2)
        rem1 = max(0, need1 - need2)
        rem2 = max(0, need2 - need1)
        
        return (common * pair_cost) + (rem1 * single1_cost) + (rem2 * single2_cost)
