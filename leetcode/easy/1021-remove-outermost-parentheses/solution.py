class Solution(object):
    def removeOuterParentheses(self, s):
        result = []
        opened = 0
        
        for char in s:
            if char == '(':
                if opened > 0:
                    result.append(char)
                opened += 1
            else:
                opened -= 1
                if opened > 0:
                    result.append(char)
                    
        return "".join(result)
