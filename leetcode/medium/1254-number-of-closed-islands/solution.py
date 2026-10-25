class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            # Base case: out of bounds or already water/visited
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 0:
                return
            
            # Sink the land by turning it into water (visited)
            grid[r][c] = 1
            
            # Explore all 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # Step 1: Flood-fill and eliminate all land connected to the borders
        for r in range(rows):
            if grid[r][0] == 0:
                dfs(r, 0)
            if grid[r][cols - 1] == 0:
                dfs(r, cols - 1)
                
        for c in range(cols):
            if grid[0][c] == 0:
                dfs(0, c)
            if grid[rows - 1][c] == 0:
                dfs(rows - 1, c)
                
        # Step 2: Any remaining 0 is part of a strictly closed island
        closed_islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    closed_islands += 1
                    dfs(r, c) # Sink the rest of this closed island
                    
        return closed_islands
