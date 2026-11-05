import bisect

class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        # Sort arr2 to enable binary search
        arr2.sort()
        distance_value = 0
        
        for val in arr1:
            # Find where 'val - d' would be inserted to maintain order
            idx = bisect.bisect_left(arr2, val - d)
            
            # If the index is within bounds and the element is <= val + d,
            # it means there is an element in arr2 within the distance 'd'
            if idx < len(arr2) and arr2[idx] <= val + d:
                continue
                
            # If no such element exists, increment the counter
            distance_value += 1
            
        return distance_value

        