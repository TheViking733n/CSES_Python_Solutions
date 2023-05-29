#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define int long long
struct Node {
    int pre;
    int sm;

    Node(int pre = 0, int sm = 0) : pre(pre), sm(sm) {}
};

Node segfunc(const Node& n1, const Node& n2) {
    int pre = max(n1.pre, n1.sm + n2.pre);
    int sm = n1.sm + n2.sm;
    return Node(pre, sm);
}

class SegmentTree {
    vector<Node> data;
    int _size;

public:
    SegmentTree(const vector<Node>& nodes) {
        int n = nodes.size();
        _size = 1 << (32 - __builtin_clz(n - 1));  // Next power of 2
        data.resize(2 * _size, Node());

        copy(nodes.begin(), nodes.end(), data.begin() + _size);
        for (int i = _size - 1; i > 0; i--)
            data[i] = segfunc(data[2 * i], data[2 * i + 1]);
    }

    Node query(int start, int stop) {
        start += _size;
        stop += _size;

        Node res_left, res_right;
        while (start < stop) {
            if (start & 1) {
                res_left = segfunc(res_left, data[start]);
                start++;
            }
            if (stop & 1) {
                stop--;
                res_right = segfunc(data[stop], res_right);
            }
            start >>= 1;
            stop >>= 1;
        }

        return segfunc(res_left, res_right);
    }

    void update(int idx, const Node& value) {
        idx += _size;
        data[idx] = value;
        idx >>= 1;
        while (idx > 0) {
            data[idx] = segfunc(data[2 * idx], data[2 * idx + 1]);
            idx >>= 1;
        }
    }

    int size() const {
        return _size;
    }
};

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, q;
    cin >> n >> q;
    vector<Node> arr(n);
    for (int i = 0; i < n; i++) {
        int val;
        cin >> val;
        arr[i] = Node(val, val);
    }
    SegmentTree seg(arr);

    for (int i = 0; i < q; i++) {
        int t, a, b;
        cin >> t >> a >> b;
        if (t == 1)
            seg.update(a - 1, Node(b, b));
        else
            cout << seg.query(a - 1, b).pre << '\n';
    }


    return 0;
}
