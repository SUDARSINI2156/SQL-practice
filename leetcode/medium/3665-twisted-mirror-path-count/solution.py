class Solution(object):
    def uniquePaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        MOD = 10**9 + 7
        
        # dp_right[i][j]: Ways to enter cell (i, j) while moving RIGHT
        # dp_down[i][j]: Ways to enter cell (i, j) while moving DOWN
        dp_right = [[0] * n for _ in range(m)]
        dp_down = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                # 1. Starting condition at (0, 0)
                if i == 0 and j == 0:
                    if j + 1 < n:
                        dp_right[i][j+1] = (dp_right[i][j+1] + 1) % MOD
                    if i + 1 < m:
                        dp_down[i+1][j] = (dp_down[i+1][j] + 1) % MOD
                
                # 2. Case: The robot successfully landed on an empty cell
                elif grid[i][j] == 0:
                    total_here = (dp_right[i][j] + dp_down[i][j]) % MOD
                    # From an empty cell, the robot can choose to go either RIGHT or DOWN
                    if j + 1 < n:
                        dp_right[i][j+1] = (dp_right[i][j+1] + total_here) % MOD
                    if i + 1 < m:
                        dp_down[i+1][j] = (dp_down[i+1][j] + total_here) % MOD
                
                # 3. Case: The robot hit a mirror cell
                else:
                    # If it entered while moving RIGHT, it is deflected DOWNwards
                    if i + 1 < m:
                        dp_down[i+1][j] = (dp_down[i+1][j] + dp_right[i][j]) % MOD
                    # If it entered while moving DOWN, it is deflected RIGHTwards
                    if j + 1 < n:
                        dp_right[i][j+1] = (dp_right[i][j+1] + dp_down[i][j]) % MOD
                        
        # The total number of valid ways to land successfully on the bottom-right corner
        return (dp_right[m-1][n-1] + dp_down[m-1][n-1]) % MOD
