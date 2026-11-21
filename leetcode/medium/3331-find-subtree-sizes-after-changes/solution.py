class Solution(object):
    def findSubtreeSizes(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: List[int]
        """
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
            
        new_parent = list(parent)
        last_seen = {}  # Maps character -> most recent ancestor node
        
        def find_new_parents(u):
            char = s[u]
            prev_ancestor = last_seen.get(char, -1)
            
            # If an ancestor with the same character exists, re-parent u
            if prev_ancestor != -1:
                new_parent[u] = prev_ancestor
                
            # Update current node as the most recent ancestor for this character
            last_seen[char] = u
            
            for v in adj[u]:
                find_new_parents(v)
                
            # Backtrack: restore the previous state for sibling branches
            last_seen[char] = prev_ancestor

        find_new_parents(0)
        
        # Build the modified tree
        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)
            
        ans = [0] * n
        
        # Calculate subtree sizes
        def get_sizes(u):
            size = 1
            for v in new_adj[u]:
                size += get_sizes(v)
            ans[u] = size
            return size
            
        get_sizes(0)
        return ans
