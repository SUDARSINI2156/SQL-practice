import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(300000)

class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type s: str
        :type queries: List[str]
        :rtype: List[bool]
        """
        # 1. Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # 2. Setup Binary Lifting for LCA & Euler Tour
        LOG = 17  # since n <= 50,000, 2^16 = 65,536
        up = [[0] * LOG for _ in range(n)]
        depth = [0] * n
        
        tin = [0] * n
        tout = [0] * n
        timer = [0]
        
        def dfs(u, p, d):
            depth[u] = d
            up[u][0] = p
            for i in range(1, LOG):
                up[u][i] = up[up[u][i-1]][i-1]
            
            timer[0] += 1
            tin[u] = timer[0]
            
            for v in adj[u]:
                if v != p:
                    dfs(v, u, d + 1)
            
            tout[u] = timer[0]
            
        dfs(0, 0, 0)
        
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            # Lift u to the same depth as v
            diff = depth[u] - depth[v]
            for i in range(LOG):
                if (diff >> i) & 1:
                    u = up[u][i]
            if u == v:
                return u
            # Lift both together
            for i in range(LOG - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]

        # 3. Fenwick Tree (BIT) for Subtree XOR Updates
        # Size is timer[0] + 2
        bit = [0] * (timer[0] + 2)
        
        def bit_update(idx, val):
            while idx < len(bit):
                bit[idx] ^= val
                idx += idx & (-idx)
                
        def bit_query(idx):
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res
            
        def update_node_char(u, old_char, new_char):
            mask = (1 << (ord(old_char) - 97)) ^ (1 << (ord(new_char) - 97))
            # Apply XOR mask to the subtree range [tin[u], tout[u]]
            bit_update(tin[u], mask)
            bit_update(tout[u] + 1, mask)

        # 4. Initialize current characters array and Fenwick Tree
        current_s = list(s)
        for i in range(n):
            mask = 1 << (ord(current_s[i]) - 97)
            bit_update(tin[i], mask)
            bit_update(tout[i] + 1, mask)
            
        # 5. Process Queries
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                if current_s[u] != c:
                    update_node_char(u, current_s[u], c)
                    current_s[u] = c
            else:
                u = int(parts[1])
                v = int(parts[2])
                lca = get_lca(u, v)
                
                # Path XOR mask calculation
                # mask(u to root) ^ mask(v to root) ^ mask(lca node itself)
                mask_u = bit_query(tin[u])
                mask_v = bit_query(tin[v])
                lca_char_mask = 1 << (ord(current_s[lca]) - 97)
                
                path_mask = mask_u ^ mask_v ^ lca_char_mask
                
                # Check if at most one bit is set
                # (path_mask & (path_mask - 1)) == 0 checks if popcount <= 1
                if path_mask == 0 or (path_mask & (path_mask - 1)) == 0:
                    ans.append(True)
                else:
                    ans.append(False)
                    
        return ans
