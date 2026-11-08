class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        row_cnt = [0] * m
        col_cnt = [0] * n
        
        # First pass: count servers in each row and column
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_cnt[i] += 1
                    col_cnt[j] += 1
                    
        # Second pass: count servers that share a row or column with another
        total_communicating = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row_cnt[i] > 1 or col_cnt[j] > 1):
                    total_communicating += 1
                    
        return total_communicating
