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