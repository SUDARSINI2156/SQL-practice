import java.util.*;

class Solution {
    public List<String> maxNumOfSubstrings(String s) {
        int n = s.length();

        int[] first = new int[26];
        int[] last = new int[26];

        Arrays.fill(first, -1);

        // Find first and last occurrence of every character
        for (int i = 0; i < n; i++) {
            int ch = s.charAt(i) - 'a';

            if (first[ch] == -1) {
                first[ch] = i;
            }

            last[ch] = i;
        }

        List<int[]> intervals = new ArrayList<>();

        // Create a valid minimum interval for every character
        for (int c = 0; c < 26; c++) {

            if (first[c] == -1) {
                continue;
            }

            int left = first[c];
            int right = last[c];

            boolean valid = true;

            for (int i = left; i <= right; i++) {
                int ch = s.charAt(i) - 'a';

                // This character appeared before left,
                // so the substring would miss an occurrence.
                if (first[ch] < left) {
                    valid = false;
                    break;
                }

                // We must include all occurrences of this character.
                right = Math.max(right, last[ch]);
            }

            if (valid) {
                intervals.add(new int[]{left, right});
            }
        }

        // Sort by ending position
        intervals.sort((a, b) -> a[1] - b[1]);

        List<String> answer = new ArrayList<>();

        int previousEnd = -1;

        // Greedily choose intervals
        for (int[] interval : intervals) {
            int left = interval[0];
            int right = interval[1];

            if (left > previousEnd) {
                answer.add(s.substring(left, right + 1));
                previousEnd = right;
            }
        }

        return answer;
    }
}