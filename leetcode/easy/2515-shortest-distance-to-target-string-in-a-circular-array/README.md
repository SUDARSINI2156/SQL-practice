# Shortest Distance to Target String in a Circular Array

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given a  **0-indexed**   **circular**  string array `words` and a string `target`. A  **circular array**  means that the array's end connects to the array's beginning.

- Formally, the next element of words[i] is words[(i + 1) % n] and the previous element of words[i] is words[(i - 1 + n) % n], where n is the length of words.

Starting from `startIndex`, you can move to either the next word or the previous word with `1` step at a time.

Return  *the  **shortest**  distance needed to reach the string*  `target`. If the string `target` does not exist in `words`, return `-1`.

 

 **Example 1:** 

```
Input: words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1
Output: 1
Explanation: We start from index 1 and can reach "hello" by
- moving 3 units to the right to reach index 4.
- moving 2 units to the left to reach index 4.
- moving 4 units to the right to reach index 0.
- moving 1 unit to the left to reach index 0.
The shortest distance to reach "hello" is 1.

```

 **Example 2:** 

```
Input: words = ["a","b","leetcode"], target = "leetcode", startIndex = 0
Output: 1
Explanation: We start from index 0 and can reach "leetcode" by
- moving 2 units to the right to reach index 2.
- moving 1 unit to the left to reach index 2.
The shortest distance to reach "leetcode" is 1.
```

 **Example 3:** 

```
Input: words = ["i","eat","leetcode"], target = "ate", startIndex = 0
Output: -1
Explanation: Since "ate" does not exist in words, we return -1.

```

 

 **Constraints:** 

- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- words[i] and target consist of only lowercase English letters.
- 0 <= startIndex < words.length

## Solution

**Language:** Java  
**Runtime:** 1 ms (beats 96.20%)  
**Memory:** 47.2 MB (beats 20.79%)  
**Submitted:** 2026-09-11T16:19:22.374Z  

```java
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
```

---

[View on LeetCode](https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/)