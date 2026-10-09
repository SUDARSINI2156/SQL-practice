class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        needed_right = 0   # Tracks how many ')' are currently needed
        insertions = 0     # Tracks total additions of '(' or ')'
        
        for char in s:
            if char == '(':
                # If we encounter an open '(' but currently need an odd number of ')',
                # it means the previous '(' only has one ')'. We must insert a ')' 
                # immediately to close it properly before starting a new group.
                if needed_right % 2 == 1:
                    insertions += 1
                    needed_right -= 1
                needed_right += 2
            else:
                # Character is ')'
                needed_right -= 1
                # If needed_right drops below 0, we have an unmatched ')' sequence.
                # We balance it by inserting an open '(' (which grants 2 ')' credits).
                if needed_right < 0:
                    insertions += 1
                    needed_right += 2
                    
        # Any remaining needed_right counts must be handled by adding closing brackets
        return insertions + needed_right
