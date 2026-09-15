# Minimum Moves to Clean the Classroom

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an `m x n` grid `classroom` where a student volunteer is tasked with cleaning up litter scattered around the room. Each cell in the grid is one of the following:

- 'S': Starting position of the student
- 'L': Litter that must be collected (once collected, the cell becomes empty)
- 'R': Reset area that restores the student's energy to full capacity, regardless of their current energy level (can be used multiple times)
- 'X': Obstacle the student cannot pass through
- '.': Empty space

You are also given an integer `energy`, representing the student's maximum energy capacity. The student starts with this energy from the starting position `'S'`.

Each move to an adjacent cell (up, down, left, or right) costs 1 unit of energy. If the energy reaches 0, the student can only continue if they are on a reset area `'R'`, which resets the energy to its  **maximum**  capacity `energy`.

Return the  **minimum**  number of moves required to collect all litter items, or `-1` if it's impossible.

 

 **Example 1:** 

 **Input:**  classroom = ["S.", "XL"], energy = 2

 **Output:**  2

 **Explanation:** 

- The student starts at cell (0, 0) with 2 units of energy.
- Since cell (1, 0) contains an obstacle 'X', the student cannot move directly downward.
- A valid sequence of moves to collect all litter is as follows: Move 1: From (0, 0) → (0, 1) with 1 unit of energy and 1 unit remaining. Move 2: From (0, 1) → (1, 1) to collect the litter 'L'.
- The student collects all the litter using 2 moves. Thus, the output is 2.

 **Example 2:** 

 **Input:**  classroom = ["LS", "RL"], energy = 4

 **Output:**  3

 **Explanation:** 

- The student starts at cell (0, 1) with 4 units of energy.
- A valid sequence of moves to collect all litter is as follows: Move 1: From (0, 1) → (0, 0) to collect the first litter 'L' with 1 unit of energy used and 3 units remaining. Move 2: From (0, 0) → (1, 0) to 'R' to reset and restore energy back to 4. Move 3: From (1, 0) → (1, 1) to collect the second litter 'L'.
- The student collects all the litter using 3 moves. Thus, the output is 3.

 **Example 3:** 

 **Input:**  classroom = ["L.S", "RXL"], energy = 3

 **Output:**  -1

 **Explanation:** 

No valid path collects all `'L'`.

 

 **Constraints:** 

- 1 <= m == classroom.length <= 20
- 1 <= n == classroom[i].length <= 20
- classroom[i][j] is one of 'S', 'L', 'R', 'X', or '.'
- 1 <= energy <= 50
- There is exactly one 'S' in the grid.
- There are at most 10 'L' cells in the grid.

## Solution

**Language:** Java  
**Runtime:** 103 ms (beats 94.51%)  
**Memory:** 48.5 MB (beats 99.97%)  
**Submitted:** 2026-09-15T03:51:34.399Z  

```java
import java.util.*;

class Solution {
    public int minMoves(String[] classroom, int energy) {
        int m = classroom.length;
        int n = classroom[0].length();

        int sr = -1, sc = -1;

        // Give every litter cell a bit number
        int[][] litterId = new int[m][n];
        for (int[] row : litterId) {
            Arrays.fill(row, -1);
        }

        int litterCount = 0;

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                char ch = classroom[r].charAt(c);

                if (ch == 'S') {
                    sr = r;
                    sc = c;
                } else if (ch == 'L') {
                    litterId[r][c] = litterCount++;
                }
            }
        }

        // No litter to collect
        if (litterCount == 0) {
            return 0;
        }

        int fullMask = (1 << litterCount) - 1;

        /*
         * best[r][c][mask] =
         * maximum remaining energy with which we've
         * reached (r, c) after collecting 'mask'.
         *
         * -1 means this state hasn't been visited.
         *
         * byte is enough because energy <= 50.
         */
        byte[][][] best = new byte[m][n][1 << litterCount];

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                Arrays.fill(best[r][c], (byte) -1);
            }
        }

        /*
         * Encode state into an int:
         *
         * row   : 5 bits  (m <= 20)
         * col   : 5 bits  (n <= 20)
         * mask  : 10 bits (<= 10 litter)
         * energy: 6 bits  (<= 50)
         */
        int SHIFT_ENERGY = 0;
        int SHIFT_MASK = 6;
        int SHIFT_COL = 16;
        int SHIFT_ROW = 21;

        int startState =
                (sr << SHIFT_ROW) |
                (sc << SHIFT_COL) |
                (0 << SHIFT_MASK) |
                energy;

        ArrayDeque<Integer> queue = new ArrayDeque<>();
        queue.offer(startState);

        best[sr][sc][0] = (byte) energy;

        int moves = 0;

        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};

        while (!queue.isEmpty()) {
            int size = queue.size();

            // Process one BFS level = one move
            while (size-- > 0) {
                int state = queue.poll();

                int r = state >>> SHIFT_ROW;
                int c = (state >>> SHIFT_COL) & 31;
                int mask = (state >>> SHIFT_MASK) & 1023;
                int curEnergy = state & 63;

                for (int d = 0; d < 4; d++) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];

                    if (nr < 0 || nr >= m || nc < 0 || nc >= n) {
                        continue;
                    }

                    if (classroom[nr].charAt(nc) == 'X') {
                        continue;
                    }

                    // Need at least 1 energy to make the move
                    if (curEnergy == 0) {
                        continue;
                    }

                    int newEnergy = curEnergy - 1;
                    int newMask = mask;

                    char cell = classroom[nr].charAt(nc);

                    // Collect litter
                    if (cell == 'L') {
                        int id = litterId[nr][nc];
                        newMask |= (1 << id);
                    }

                    // Reset energy when entering R
                    if (cell == 'R') {
                        newEnergy = energy;
                    }

                    // All litter collected
                    if (newMask == fullMask) {
                        return moves + 1;
                    }

                    /*
                     * If we've already reached this state with
                     * >= energy, this state is useless.
                     */
                    if (best[nr][nc][newMask] >= newEnergy) {
                        continue;
                    }

                    best[nr][nc][newMask] = (byte) newEnergy;

                    int newState =
                            (nr << SHIFT_ROW) |
                            (nc << SHIFT_COL) |
                            (newMask << SHIFT_MASK) |
                            newEnergy;

                    queue.offer(newState);
                }
            }

            moves++;
        }

        return -1;
    }
}
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/)