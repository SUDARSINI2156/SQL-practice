# Maximum Score of Non-overlapping Intervals

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given a 2D integer array `intervals`, where `intervals[i] = [li, ri, weighti]`. Interval `i` starts at position `li` and ends at `ri`, and has a weight of `weighti`. You can choose  *up to*  4  **non-overlapping**  intervals. The  **score**  of the chosen intervals is defined as the total sum of their weights.

Return the lexicographically smallest array of at most 4 indices from `intervals` with  **maximum**  score, representing your choice of non-overlapping intervals.

Two intervals are said to be  **non-overlapping**  if they do not share any points. In particular, intervals sharing a left or right boundary are considered overlapping.

 

 **Example 1:** 

 **Input:**  intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]

 **Output:**  [2,3]

 **Explanation:** 

You can choose the intervals with indices 2, and 3 with respective weights of 5, and 3.

 **Example 2:** 

 **Input:**  intervals = [[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]

 **Output:**  [1,3,5,6]

 **Explanation:** 

You can choose the intervals with indices 1, 3, 5, and 6 with respective weights of 7, 6, 3, and 5.

 

 **Constraints:** 

- 1 <= intevals.length <= 5 * 104
- intervals[i].length == 3
- intervals[i] = [li, ri, weighti]
- 1 <= li <= ri <= 109
- 1 <= weighti <= 109

## Solution

**Language:** Java  
**Runtime:** 132 ms (beats 85.18%)  
**Memory:** 165.8 MB (beats 70.37%)  
**Submitted:** 2026-09-12T03:39:21.751Z  

```java
import java.util.*;

class Solution {

    static class Interval {
        int start, end, weight, index;

        Interval(int start, int end, int weight, int index) {
            this.start = start;
            this.end = end;
            this.weight = weight;
            this.index = index;
        }
    }

    static class State {
        long score;
        List<Integer> indices;

        State(long score, List<Integer> indices) {
            this.score = score;
            this.indices = indices;
        }
    }

    Interval[] arr;
    State[][] dp;

    public int[] maximumWeight(List<List<Integer>> intervals) {

        int n = intervals.size();

        arr = new Interval[n];

        for (int i = 0; i < n; i++) {
            arr[i] = new Interval(
                intervals.get(i).get(0),
                intervals.get(i).get(1),
                intervals.get(i).get(2),
                i
            );
        }

        Arrays.sort(arr, (a, b) -> {
            if (a.start != b.start)
                return Integer.compare(a.start, b.start);

            return Integer.compare(a.end, b.end);
        });

        dp = new State[n + 1][5];

        State answer = solve(0, 4);

        Collections.sort(answer.indices);

        int[] result = new int[answer.indices.size()];

        for (int i = 0; i < answer.indices.size(); i++) {
            result[i] = answer.indices.get(i);
        }

        return result;
    }

    private State solve(int pos, int remaining) {

        if (pos == arr.length || remaining == 0) {
            return new State(0, new ArrayList<>());
        }

        if (dp[pos][remaining] != null) {
            return dp[pos][remaining];
        }

        // Option 1: Skip current interval
        State skip = solve(pos + 1, remaining);

        // Option 2: Take current interval
        int next = findNext(pos);

        State future = solve(next, remaining - 1);

        List<Integer> takeIndices = new ArrayList<>();
        takeIndices.add(arr[pos].index);
        takeIndices.addAll(future.indices);

        State take = new State(
            arr[pos].weight + future.score,
            takeIndices
        );

        State best = better(take, skip);

        dp[pos][remaining] = best;

        return best;
    }

    private int findNext(int pos) {

        int low = pos + 1;
        int high = arr.length;

        while (low < high) {

            int mid = low + (high - low) / 2;

            // Must be strictly greater because
            // sharing a boundary means overlapping
            if (arr[mid].start > arr[pos].end) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }

        return low;
    }

    private State better(State a, State b) {

        if (a.score > b.score) {
            return a;
        }

        if (a.score < b.score) {
            return b;
        }

        List<Integer> x = new ArrayList<>(a.indices);
        List<Integer> y = new ArrayList<>(b.indices);

        Collections.sort(x);
        Collections.sort(y);

        for (int i = 0; i < Math.min(x.size(), y.size()); i++) {

            if (!x.get(i).equals(y.get(i))) {
                return x.get(i) < y.get(i) ? a : b;
            }
        }

        return x.size() <= y.size() ? a : b;
    }
}
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/)