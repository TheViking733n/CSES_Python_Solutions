#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    // Fast IO
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, k, x, M = 1e9+7;
    cin >> n >> k;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> x, arr[i] = x;
    sort(arr.begin(), arr.end());
    vector<int> dp(k+1, 0);
    dp[0] = 1;
    for (int i = 1; i <= k; i++) {
        for (auto coin: arr) {
            if (i - coin < 0) break;
            dp[i] += dp[i - coin];
            dp[i] %= M;
        }
    }
    cout << dp[k];
    
    return 0;
}