class Solution {
    public int reverseDegree(String s) {
        int totalDegree = 0;
        
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            int stringIndex = i + 1; // Menggunakan 1-indexed
            
            // 'a' = 26, 'b' = 25, ..., 'z' = 1
            int reversedAlphabetPos = 26 - (ch - 'a');
            
            // Tambahkan hasil perkalian ke total
            totalDegree += reversedAlphabetPos * stringIndex;
        }
        
        return totalDegree;
    }
}
