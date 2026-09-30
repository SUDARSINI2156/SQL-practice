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
