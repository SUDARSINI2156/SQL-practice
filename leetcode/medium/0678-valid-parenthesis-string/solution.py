class Solution(object):
    def checkValidString(self, s):
        cmin = 0  # Jumlah minimum '(' yang harus ditutup
        cmax = 0  # Jumlah maksimum '(' yang bisa ditutup
        
        for char in s:
            if char == '(':
                cmin += 1
                cmax += 1
            elif char == ')':
                cmin -= 1
                cmax -= 1
            elif char == '*':
                cmin -= 1  # '*' dianggap sebagai ')'
                cmax += 1  # '*' dianggap sebagai '('
            
            if cmax < 0:
                return False
            
            cmin = max(cmin, 0)
            
        return cmin == 0
