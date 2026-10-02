class Solution(object):
    def generateParenthesis(self, n):
        result = []
        
        def backtrack(current_str, open_count, close_count):
            # Jika panjang string sudah mencapai 2 * n, kombinasi selesai
            if len(current_str) == 2 * n:
                result.append(current_str)
                return
            
            # Tambahkan kurung buka jika jumlahnya belum mencapai n
            if open_count < n:
                backtrack(current_str + "(", open_count + 1, close_count)
                
            # Tambahkan kurung tutup jika jumlahnya lebih sedikit dari kurung buka
            if close_count < open_count:
                backtrack(current_str + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result
