class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        sorted_s = "".join(sorted(s))
        
        # Case 0: String is already sorted
        if s == sorted_s:
            return 0
            
        n = len(s)
        
        # Case 1: A boundary character is already in its correct final home.
        if s[0] == sorted_s[0] or s[n-1] == sorted_s[n-1]:
            return 1
            
        # Case 2: The absolute max is at the front and absolute min is at the back
        if s[0] == sorted_s[n-1] and s[n-1] == sorted_s[0]:
            
            # Check if the middle section contains only a uniform repeating character
            # (or is empty, which handles n=2 and n=3 automatically)
            middle_section = s[1:n-1]
            if len(set(middle_section)) <= 1:
                if n == 2:
                    return -1 # "gf" -> Completely impossible
                else:
                    return 3  # "edc", "srrp" -> Requires 3 rolling operations
                
        # Case 3: All other mixed configurations can be solved in 2 steps
        return 2
