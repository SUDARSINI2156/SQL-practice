class Solution(object):
    def reverseParentheses(self, s):
        stack = []
        
        for char in s:
            if char == ')':
                portion = []
                while stack and stack[-1] != '(':
                    portion.append(stack.pop())
                
                if stack:
                    stack.pop()  # Hapus '('
                
                stack.extend(portion)
            else:
                stack.append(char)
                
        return "".join(stack)
