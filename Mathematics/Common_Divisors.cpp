#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <cmath>
using namespace std;

int gcd(int a, int b) {
    if (a == 0) {
        return b;
    }
    return gcd(b % a, a);
}

int max(int a, int b) {
    return (a > b) ? a : b;
}

const int MAX_N = 1000001;

vector<int> spf(MAX_N);

void computeSmallestPrimeFactor() {
    for (int i = 2; i < MAX_N; i++) {
        if (spf[i] == i) {
            for (int j = i * i; j < MAX_N; j += i) {
                if (spf[j] == j) {
                    spf[j] = i;
                }
            }
        }
    }
}

unordered_map<int, int> factors(int x) {
    unordered_map<int, int> res;
    while (x != 1) {
        res[spf[x]]++;
        x /= spf[x];
    }
    return res;
}

int main() {
    // ios_base::sync_with_stdio(false);
    // cin.tie(NULL);

    computeSmallestPrimeFactor();

    int n;
    cin >> n;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    sort(arr.begin(), arr.end());

    vector<int> a2;
    a2.push_back(arr[0]);
    a2.push_back(arr[1]);

    for (int i = 2; i < n; i++) {
        if (arr[i] != arr[i - 2]) {
            a2.push_back(arr[i]);
        }
    }

    n = a2.size();
    // a2 = a2;

    unordered_map<int, vector<pair<int, int>>> m;
    for (int i = 0; i < n; i++) {
        unordered_map<int, int> pf = factors(a2[i]);
        for (auto it = pf.begin(); it != pf.end(); it++) {
            int p = it->first;
            int e = it->second;
            m[p].push_back(make_pair(e, i));
        }
    }

    int ans = 1;
    for (auto it = m.begin(); it != m.end(); it++) {
        vector<pair<int, int>>& v = it->second;
        sort(v.begin(), v.end(), greater<pair<int, int>>());
        while (v.size() > 2) {
            if (v.back().first < v[1].first) {
                v.pop_back();
            } else {
                break;
            }
        }
        for (int i = 0; i < v.size() - 1; i++) {
            for (int j = i + 1; j < v.size(); j++) {
                int i1 = v[i].second;
                int i2 = v[j].second;
                ans = max(ans, gcd(a2[i1], a2[i2]));
            }
        }
    }

    cout << ans;

    return 0;
}
