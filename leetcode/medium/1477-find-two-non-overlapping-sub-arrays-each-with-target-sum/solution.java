class Solution {
    public int minSumOfLengths(int[] arr, int target) {

        int n = arr.length;

        // best[i] = shortest valid subarray ending at or before i
        int[] best = new int[n];

        int left = 0;
        int sum = 0;

        int INF = n + 1;
        int shortest = INF;
        int answer = INF;

        for (int right = 0; right < n; right++) {

            sum += arr[right];

            // Make window sum <= target
            while (sum > target) {
                sum -= arr[left];
                left++;
            }

            // We found a subarray whose sum is target
            if (sum == target) {

                int currentLength = right - left + 1;

                // Check if there is a previous non-overlapping subarray
                if (left > 0 && best[left - 1] != INF) {
                    answer = Math.min(
                        answer,
                        currentLength + best[left - 1]
                    );
                }

                // Keep the shortest subarray seen so far
                shortest = Math.min(shortest, currentLength);
            }

            // Store shortest subarray found up to right
            if (right == 0) {
                best[right] = shortest;
            } else {
                best[right] = Math.min(best[right - 1], shortest);
            }
        }

        if (answer == INF) {
            return -1;
        }

        return answer;
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna