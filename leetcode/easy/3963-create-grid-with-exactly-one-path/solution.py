class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        # Create an m x n grid filled entirely with obstacles
        grid = [['#'] * n for _ in range(m)]
        
        # Fill the first row with free cells
        for j in range(n):
            grid[0][j] = '.'
            
        # Fill the last column with free cells
        for i in range(m):
            grid[i][n - 1] = '.'
            
        # Convert each row from a list of characters to a string
        return ["".join(row) for row in grid]
