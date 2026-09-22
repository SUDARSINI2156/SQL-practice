import java.util.Arrays;

class Solution {
    int K;
    
    class Node {
        int prod;
        int[] cnt;
        
        Node(int k) {
            this.prod = 1;
            this.cnt = new int[k];
        }
    }
    
    Node[] tree;
    
    private Node merge(Node left, Node right) {
        Node res = new Node(K);
        res.prod = (left.prod * right.prod) % K;
        
        for (int i = 0; i < K; i++) {
            res.cnt[i] += left.cnt[i];
            int targetRem = (left.prod * i) % K;
            res.cnt[targetRem] += right.cnt[i];
        }
        return res;
    }
    
    private void build(int node, int start, int end, int[] nums) {
        if (start == end) {
            tree[node] = new Node(K);
            int val = nums[start] % K;
            tree[node].prod = val;
            tree[node].cnt[val] = 1;
            return;
        }
        int mid = (start + end) / 2;
        build(2 * node, start, mid, nums);
        build(2 * node + 1, mid + 1, end, nums);
        tree[node] = merge(tree[2 * node], tree[2 * node + 1]);
    }
    
    private void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            int rem = val % K;
            Arrays.fill(tree[node].cnt, 0);
            tree[node].prod = rem;
            tree[node].cnt[rem] = 1;
            return;
        }
        int mid = (start + end) / 2;
        if (idx <= mid) {
            update(2 * node, start, mid, idx, val);
        } else {
            update(2 * node + 1, mid + 1, end, idx, val);
        }
        tree[node] = merge(tree[2 * node], tree[2 * node + 1]);
    }
    
    private Node query(int node, int start, int end, int l, int r) {
        if (l <= start && end <= r) {
            return tree[node];
        }
        int mid = (start + end) / 2;
        if (r <= mid) {
            return query(2 * node, start, mid, l, r);
        }
        if (l > mid) {
            return query(2 * node + 1, mid + 1, end, l, r);
        }
        Node leftRes = query(2 * node, start, mid, l, mid);
        Node rightRes = query(2 * node + 1, mid + 1, end, mid + 1, r);
        return merge(leftRes, rightRes);
    }

    // Nama fungsi diubah menjadi resultArray sesuai dengan driver system
    public int[] resultArray(int[] nums, int k, int[][] queries) {
        this.K = k;
        int n = nums.length;
        tree = new Node[4 * n];
        
        build(1, 0, n - 1, nums);
        
        int[] result = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            // Memperbaiki indeks ekstraksi query dari queries[i] menjadi queries[i][j]
            int idx = queries[i][0];
            int val = queries[i][1];
            int start = queries[i][2];
            int x = queries[i][3];
            
            // 1. Update nilai elemen secara permanen
            update(1, 0, n - 1, idx, val);
            
            // 2. Cari hasil query untuk rentang [start, n-1]
            Node resNode = query(1, 0, n - 1, start, n - 1);
            
            // 3. Simpan total cara yang sisa modulonya adalah x
            result[i] = resNode.cnt[x];
        }
        
        return result;
    }
}
