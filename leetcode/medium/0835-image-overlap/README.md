# Image Overlap

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given two images, `img1` and `img2`, represented as binary, square matrices of size `n x n`. A binary matrix has only `0`s and `1`s as values.

We  **translate**  one image however we choose by sliding all the `1` bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the  **overlap**  by counting the number of positions that have a `1` in  **both**  images.

Note also that a translation does  **not**  include any kind of rotation. Any `1` bits that are translated outside of the matrix borders are erased.

Return  *the largest possible overlap*.

 

 **Example 1:** 

```
Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
Output: 3
Explanation: We translate img1 to right by 1 unit and down by 1 unit.

The number of positions that have a 1 in both images is 3 (shown in red).

```

 **Example 2:** 

```
Input: img1 = [[1]], img2 = [[1]]
Output: 1

```

 **Example 3:** 

```
Input: img1 = [[0]], img2 = [[0]]
Output: 0

```

 

 **Constraints:** 

- n == img1.length == img1[i].length
- n == img2.length == img2[i].length
- 1 <= n <= 30
- img1[i][j] is either 0 or 1.
- img2[i][j] is either 0 or 1.

## Solution

**Language:** Python  
**Runtime:** 394 ms (beats 73.24%)  
**Memory:** 12.9 MB (beats 14.19%)  
**Submitted:** 2026-09-30T07:39:56.822Z  

```py
from collections import Counter

class Solution(object):
    def largestOverlap(self, img1, img2):
        n = len(img1)
        
        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        vector_counts = Counter()
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                transformation_vector = (r2 - r1, c2 - c1)
                vector_counts[transformation_vector] += 1
                
        return max(vector_counts.values()) if vector_counts else 0

```

---

[View on LeetCode](https://leetcode.com/problems/image-overlap/)