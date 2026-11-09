import heapq
import bisect

class Solution(object):
    def busiestServers(self, k, arrival, load):
        """
        :type k: int
        :type arrival: List[int]
        :type load: List[int]
        :rtype: List[int]
        """
        busy = []  # Min-heap of (free_time, server_id)
        available = list(range(k))  # Min-heap of available server IDs
        heapq.heapify(available)
        
        requests_handled = [0] * k
        
        for i, (arr_time, l_time) in enumerate(zip(arrival, load)):
            # Free up servers that have finished their tasks by arrival time
            while busy and busy[0][0] <= arr_time:
                _, freed_server = heapq.heappop(busy)
                # Maintain the available list in sorted order for binary search
                bisect.insort(available, freed_server)
                
            if not available:
                continue  # All servers are busy; drop request
            
            # Find the first available server >= (i % k)
            target = i % k
            idx = bisect.bisect_left(available, target)
            
            # If no server >= target is available, wrap around to the first available server
            if idx == len(available):
                idx = 0
                
            server_id = available.pop(idx)
            requests_handled[server_id] += 1
            heapq.heappush(busy, (arr_time + l_time, server_id))
            
        max_handled = max(requests_handled)
        return [idx for idx, count in enumerate(requests_handled) if count == max_handled]
