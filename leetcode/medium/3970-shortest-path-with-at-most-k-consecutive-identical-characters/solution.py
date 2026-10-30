import heapq
from collections import defaultdict

class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            
        # Min-heap: (cost, node, count_of_current_label)
        pq = [(0, 0, 1)]
        # Track minimum cost to reach (node, count)
        dist = {}
        
        while pq:
            cost, u, count = heapq.heappop(pq)
            
            if u == n - 1:
                return cost
                
            if (u, count) in dist and dist[(u, count)] <= cost:
                continue
            dist[(u, count)] = cost
            
            for v, w in graph[u]:
                if labels[v] == labels[u]:
                    next_count = count + 1
                else:
                    next_count = 1
                    
                if next_count <= k:
                    if (v, next_count) not in dist or cost + w < dist.get((v, next_count), float('inf')):
                        heapq.heappush(pq, (cost + w, v, next_count))
                        
        return -1
