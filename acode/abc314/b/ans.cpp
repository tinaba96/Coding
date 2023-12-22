#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i = 0; i < (n); ++i)

int main() {
  int n;
  cin >> n;
  vector<int> c(n);
  vector<vector<int>> a(n);
  rep(i,n) {
    cin >> c[i];
    a[i] = vector<int>(c[i]);
    rep(j,c[i]) cin >> a[i][j];
  }
  int x;
  cin >> x;

  int cmin = 100;
  vector<int> ans;
  rep(i,n) {
    bool p = false;
    rep(j,c[i]) if (a[i][j] == x) p = true;
    if (!p) continue;
    if (cmin < c[i]) continue;
    if (cmin > c[i]) {
      cmin = c[i];
      ans = vector<int>();
    }
    ans.push_back(i+1);
  }

  cout << ans.size() << endl;
  for (int i : ans) cout << i << ' ';
  cout << endl;
  return 0;
}
