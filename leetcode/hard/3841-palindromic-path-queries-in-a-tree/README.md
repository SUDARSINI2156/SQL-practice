# Palindromic Path Queries in a Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given an undirected tree with `n` nodes labeled 0 to `n - 1`. This is represented by a 2D array `edges` of length `n - 1`, where `edges[i] = [ui, vi]` indicates an undirected edge between nodes `ui` and `vi`.

You are also given a string `s` of length `n` consisting of lowercase English letters, where `s[i]` represents the character assigned to node `i`.

You are also given a string array `queries`, where each `queries[i]` is either:

- "update ui c": Change the character at node ui to c. Formally, update s[ui] = c.
- "query ui vi": Determine whether the string formed by the characters on the unique path from ui to vi (inclusive) can be rearranged into a palindrome.

Return a boolean array `answer`, where `answer[j]` is `true` if the `jth` query of type `"query ui vi"​​​​​​​` can be rearranged into a  **palindrome**, and `false` otherwise.

 

 **Example 1:** 

 **Input:**  n = 3, edges = [[0,1],[1,2]], s = "aac", queries = ["query 0 2","update 1 b","query 0 2"]

 **Output:**  [true,false]

 **Explanation:** 

- "query 0 2": Path 0 → 1 → 2 gives "aac", which can be rearranged to form "aca", a palindrome. Thus, answer[0] = true.
- "update 1 b": Update node 1 to 'b', now s = "abc".
- "query 0 2": Path characters are "abc", which cannot be rearranged to form a palindrome. Thus, answer[1] = false.

Thus, `answer = [true, false]`.

 **Example 2:** 

 **Input:**  n = 4, edges = [[0,1],[0,2],[0,3]], s = "abca", queries = ["query 1 2","update 0 b","query 2 3","update 3 a","query 1 3"]

 **Output:**  [false,false,true]

 **Explanation:** 

- "query 1 2": Path 1 → 0 → 2 gives "bac", which cannot be rearranged to form a palindrome. Thus, answer[0] = false.
- "update 0 b": Update node 0 to 'b', now s = "bbca".
- "query 2 3": Path 2 → 0 → 3 gives "cba", which cannot be rearranged to form a palindrome. Thus, answer[1] = false.
- "update 3 a": Update node 3 to 'a', s = "bbca".
- "query 1 3": Path 1 → 0 → 3 gives "bba", which can be rearranged to form "bab", a palindrome. Thus, answer[2] = true.

Thus, `answer = [false, false, true]`.

 

 **Constraints:** 

- 1 <= n == s.length <= 5 * 104
- edges.length == n - 1
- edges[i] = [ui, vi]
- 0 <= ui, vi <= n - 1
- s consists of lowercase English letters.
- The input is generated such that edges represents a valid tree.
- 1 <= queries.length <= 5 * 104​​​​​​​queries[i] = "update ui c" or queries[i] = "query ui vi" 0 <= ui, vi <= n - 1 c is a lowercase English letter.

## Solution

**Language:** Python  
**Runtime:** 3154 ms (beats 10.00%)  
**Memory:** 108.5 MB (beats 10.00%)  
**Submitted:** 2026-10-29T15:47:23.783Z  

```py
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

```

---

[View on LeetCode](https://leetcode.com/problems/palindromic-path-queries-in-a-tree/)