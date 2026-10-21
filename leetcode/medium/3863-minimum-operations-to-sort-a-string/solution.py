
class Solution:
    def minOperations(self, s):
        n = len(s)
        sorted_s = ''.join(sorted(s))

        if s == sorted_s:
            return 0

        if n == 2:
            return -1

        smallest = min(s)
        largest = max(s)

        if s[0] == smallest or s[-1] == largest:
            return 1

        if s[0] == largest and s[-1] == smallest:
            if s.count(largest) == 1 and s.count(smallest) == 1:
                return 3

        return 2
