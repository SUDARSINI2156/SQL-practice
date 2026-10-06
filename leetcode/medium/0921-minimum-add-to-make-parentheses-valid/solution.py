class Solution(object):
    def minAddToMakeValid(self, s):
        buka = 0
        tambah = 0
        
        for char in s:
            if char == '(':
                buka += 1
            else:  # char == ')'
                if buka > 0:
                    buka -= 1
                else:
                    tambah += 1
                    
        return tambah + buka
