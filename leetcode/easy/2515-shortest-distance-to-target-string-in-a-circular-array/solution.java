class Solution {
    public int closestTarget(String[] words, String target, int startIndex) {

        int minDistance = Integer.MAX_VALUE;

        for (int i = 0; i < words.length; i++) {

            if (words[i].equals(target)) {

                int distance = Math.abs(i - startIndex);

                distance = Math.min(distance, words.length - distance);

                if (distance < minDistance) {
                    minDistance = distance;
                }
            }
        }

        if (minDistance == Integer.MAX_VALUE) {
            return -1;
        }

        return minDistance;
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna