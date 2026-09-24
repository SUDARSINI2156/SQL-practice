class Solution {
    public int smallestIndex(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            if (getDigitSum(nums[i]) == i) {
                return i; // Karena bergerak dari 0, ini pasti indeks terkecil
            }
        }
        return -1; // Jika tidak ada indeks yang memenuhi syarat
    }

    // Fungsi pembantu untuk menghitung jumlah digit secara matematis
    private int getDigitSum(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}
