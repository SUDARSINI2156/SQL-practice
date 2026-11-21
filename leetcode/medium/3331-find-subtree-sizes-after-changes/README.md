# Find Subtree Sizes After Changes

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a tree rooted at node 0 that consists of `n` nodes numbered from `0` to `n - 1`. The tree is represented by an array `parent` of size `n`, where `parent[i]` is the parent of node `i`. Since node 0 is the root, `parent[0] == -1`.

You are also given a string `s` of length `n`, where `s[i]` is the character assigned to node `i`.

We make the following changes on the tree  **one**  time  **simultaneously**  for all nodes `x` from `1` to `n - 1`:

- Find the closest node y to node x such that y is an ancestor of x, and s[x] == s[y].
- If node y does not exist, do nothing.
- Otherwise, remove the edge between x and its current parent and make node y the new parent of x by adding an edge between them.

Return an array `answer` of size `n` where `answer[i]` is the  **size**  of the subtree rooted at node `i` in the  **final**  tree.

 

Original
Python
 **Example 1:** 

 **Input:**  parent = [-1,0,0,1,1,1], s = "abaabc"

 **Output:**  [6,3,1,1,1,1]

 **Explanation:** 

The parent of node 3 will change from node 1 to node 0.

 **Example 2:** 

 **Input:**  parent = [-1,0,4,0,1], s = "abbba"

 **Output:**  [5,2,1,1,1]

 **Explanation:** 

The following changes will happen at the same time:

- The parent of node 4 will change from node 1 to node 0.
- The parent of node 2 will change from node 4 to node 1.

 

 **Constraints:** 

- n == parent.length == s.length
- 1 <= n <= 105
- 0 <= parent[i] <= n - 1 for all i >= 1.
- parent[0] == -1
- parent represents a valid tree.
- s consists only of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 1659 ms (beats 30.00%)  
**Memory:** 160.6 MB (beats 10.00%)  
**Submitted:** 2026-11-21T16:14:27.690Z  

```py
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

```

---

[View on LeetCode](https://leetcode.com/problems/find-subtree-sizes-after-changes/)