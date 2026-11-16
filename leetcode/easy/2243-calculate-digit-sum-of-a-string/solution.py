class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s) > k:
            next_s = []
            # Iterate through the string in steps of size k
            for i in range(0, len(s), k):
                group = s[i : i + k]
                # Calculate the sum of digits in the current group
                group_sum = sum(int(digit) for digit in group)
                next_s.append(str(group_sum))
            
            # Join all group sums to form the new string for the next round
            s = "".join(next_s)
            
        return s
 
        