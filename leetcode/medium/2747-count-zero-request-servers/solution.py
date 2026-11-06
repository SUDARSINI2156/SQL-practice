class Solution(object):
    def countServers(self, n, logs, x, queries):
        """
        :type n: int
        :type logs: List[List[int]]
        :type x: int
        :type queries: List[int]
        :rtype: List[int]
        """
        # Sort logs based on time (log[1])
        logs.sort(key=lambda log: log[1])
        
        # Store queries with their original indices and sort them by time
        sorted_queries = sorted(enumerate(queries), key=lambda q: q[1])
        
        ans = [0] * len(queries)
        server_counts = {}  # Tracks server_id -> frequency in current window
        
        left = 0
        right = 0
        m = len(logs)
        
        for original_idx, query_time in sorted_queries:
            # Expand the window: Add logs that are <= query_time
            while right < m and logs[right][1] <= query_time:
                server_id = logs[right][0]
                server_counts[server_id] = server_counts.get(server_id, 0) + 1
                right += 1
                
            # Shrink the window: Remove logs that are < query_time - x
            while left < m and logs[left][1] < query_time - x:
                server_id = logs[left][0]
                if server_id in server_counts:
                    server_counts[server_id] -= 1
                    if server_counts[server_id] == 0:
                        del server_counts[server_id]
                left += 1
            
            # Number of inactive servers = total - active
            ans[original_idx] = n - len(server_counts)
            
        return ans
