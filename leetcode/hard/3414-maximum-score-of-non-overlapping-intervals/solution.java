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