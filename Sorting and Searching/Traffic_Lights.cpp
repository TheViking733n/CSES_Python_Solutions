#include <iostream>
#include <set>

using namespace std;
#define int long long int

signed main() {
    ios::sync_with_stdio(false);
	cin.tie(NULL);
    
    int k, n, cur;
    cin >> k >> n;
    multiset<int> lights;
    multiset<int> pq;
    lights.insert(0);
    lights.insert(k);
    pq.insert(-k);
    while (n --> 0) {
        cin >> cur;
        auto r = lights.upper_bound(cur);
        auto l = r;
        l--;
        pq.erase(pq.find(-((*r) - (*l))));
        lights.insert(cur);
        pq.insert(-((*r) - cur));
        pq.insert(-(cur - (*l)));
        cout << (-*pq.begin()) << " ";
    }
    cout << endl;

    return 0;
}