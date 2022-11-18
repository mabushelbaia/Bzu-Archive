#include <bits/stdc++.h>
using namespace std;
 
#define ll long long
 
int main() {
    int t;
    cin >> t;
    while (t--){
        int n;
        ll max;
        cin >> n >> max;
        vector<ll> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        int limit = 1<<n;
        vector<pair<ll, ll>> dp(limit);
        dp[0] = {1, 0};
        for(int mask = 1; mask < limit; mask++){
            pair<ll, ll> bestResult = {INT_MAX, INT_MAX};
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) == 0) continue;
                auto res = dp[mask ^ (1 << i)];
                if (res.second + a[i] <= max) {
                    res.second += a[i];
                } 
                else {
                    res.first += 1;
                    res.second = a[i];
                }
                bestResult = min(bestResult, res);
            }
            dp[mask] = bestResult;
        }
        cout << dp[limit - 1].first << endl;
    }
    return 0;
}
