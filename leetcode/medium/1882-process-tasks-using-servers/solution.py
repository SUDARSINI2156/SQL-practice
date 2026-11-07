import heapq

class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        # free_servers: min-heap storing (weight, index)
        free_servers = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(free_servers)
        
        # used_servers: min-heap storing (free_time, weight, index)
        used_servers = []
        
        ans = []
        t = 0
        
        for j, task_time in enumerate(tasks):
            # The current time cannot be behind the task arrival index j
            t = max(t, j)
            
            # If all servers are currently busy, fast-forward time to when the earliest server frees up
            if not free_servers:
                t = used_servers[0][0]
                
            # Free up all servers whose processing finishes at or before current time t
            while used_servers and used_servers[0][0] <= t:
                free_time, weight, idx = heapq.heappop(used_servers)
                heapq.heappush(free_servers, (weight, idx))
                
            # Assign the task to the best available free server
            weight, idx = heapq.heappop(free_servers)
            ans.append(idx)
            heapq.heappush(used_servers, (t + task_time, weight, idx))
            
        return ans
