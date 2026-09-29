class Solution(object):
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        
        # Jika panjang total jalur ganjil, tidak mungkin membentuk kurung valid
        if (m + n - 1) % 2 != 0:
            return False
            
        # Jika sel awal adalah ')' atau sel akhir adalah '(', jalur tidak valid
        if grid[0][0] == ")" or grid[m - 1][n - 1] == "(":
            return False
            
        memo = set()
        
        def dfs(r, c, balance):
            # Perbarui balance berdasarkan karakter saat ini
            if grid[r][c] == "(":
                balance += 1
            else:
                balance -= 1
                
            # Jika kelebihan ')', jalur langsung tidak valid
            if balance < 0:
                return False
                
            # Jika sampai di ujung bawah-kanan
            if r == m - 1 and c == n - 1:
                return balance == 0
                
            # Cek memo untuk menghindari pengerjaan ulang
            if (r, c, balance) in memo:
                return False
            memo.add((r, c, balance))
            
            # Bergerak ke bawah atau ke kanan
            if r + 1 < m and dfs(r + 1, c, balance):
                return True
            if c + 1 < n and dfs(r, c + 1, balance):
                return True
                
            return False
            
        return dfs(0, 0, 0)
