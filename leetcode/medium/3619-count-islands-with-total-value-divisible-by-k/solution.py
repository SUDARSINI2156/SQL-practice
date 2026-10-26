class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
            
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        divisible_island_count = 0
        
        # Directions for 4-directional movement (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for i in range(m):
            for j in range(n):
                # A positive integer represents unvisited land
                if grid[i][j] > 0 and not visited[i][j]:
                    island_sum = 0
                    stack = [(i, j)]
                    visited[i][j] = True
                    
                    # Explore the full island iteratively
                    while stack:
                        r, c = stack.pop()
                        island_sum += grid[r][c]
                        
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            # Ensure bounds, evaluate land, and verify it hasn't been visited
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                stack.append((nr, nc))
                    
                    # Check if the complete island sum is divisible by k
                    if island_sum % k == 0:
                        divisible_island_count += 1
                        
        return divisible_island_count
