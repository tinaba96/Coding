#include "bits/stdc++.h"
using namespace std;

#define endl '\n'

const int N = 2001, mod = 998244353;
int dp[N][N][2];
vector<int> adj[N];
int n, m, k, s, t, x;

int solve(int v, int steps, int parity) {
    int &st = dp[v][steps][parity]; // memo
    if (st != -1) return st; // there is no  case that st = 0 since node that you visit is the time that the st for the same situation has already completed 
    // because it will not goes back to same node with same step. This can be happened (memo can be used) only after the st for this node has already completed.

    if (steps == 0) {
        return st = (v == t && parity == 0);
    }

    if (v == x) parity ^= 1;

    st = 0;
    for (int c : adj[v]) {
        st = (st + solve(c, steps - 1, parity)) % mod;
    }
    return st;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m >> k >> s >> t >> x;
    for (int i = 0; i < m; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    memset(dp, -1, sizeof dp);
    cout << solve(s, k, 0) << endl;
}


