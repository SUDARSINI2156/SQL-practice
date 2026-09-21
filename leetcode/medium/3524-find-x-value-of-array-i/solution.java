class Solution {
    public long[] resultArray(int[] nums, int k) {
        long[] result = new long[k];
        long[] dp = new long[k];
        
        for (int num : nums) {
            int v = num % k;
            long[] nextDp = new long[k];
            
            // Kalikan seluruh subarray dari indeks sebelumnya dengan elemen saat ini
            for (int x = 0; x < k; x++) {
                if (dp[x] > 0) {
                    nextDp[(x * v) % k] += dp[x];
                }
            }
            
            // Tambahkan subarray tunggal baru yang dimulai dari elemen saat ini
            nextDp[v] += 1;
            
            // Salin state ke dp dan akumulasikan ke result
            dp = nextDp;
            for (int x = 0; x < k; x++) {
                result[x] += dp[x];
            }
        }
        
        return result;
    }
}
