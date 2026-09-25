class Solution:
    def braceExpansionII(self, expression):
        s = {expression}
        while any('{' in x for x in s):
            next_s = set()
            for expr in s:
                i = 0
                while i < len(expr) and expr[i] != '}':
                    i += 1
                j = i
                while j >= 0 and expr[j] != '{':
                    j -= 1
                left = expr[:j]
                right = expr[i+1:]
                middle = expr[j+1:i].split(',')
                for m in middle:
                    next_s.add(left + m + right)
            s = next_s
        return sorted(list(s))
