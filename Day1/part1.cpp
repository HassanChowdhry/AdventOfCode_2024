#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back
#define flash ios_base::sync_with_stdio(false);cin.tie(NULL);
#define loop(n) for(int i=0;i<n;++i)
#define ln "\n"

void solve() {
  int n = 1000, l, r;
  vector<int> left, right;
  loop(n) {
    cin >> l >> r;
    left.pb(l); right.pb(r);
  }

  sort(left.begin(), left.end());
  sort(right.begin(), right.end());

  ll ans = 0;
  loop(n) 
    { ans += abs(left[i] - right[i]); }

  cout << ans;
}

int main() {
  flash;
  solve();
  return 0;
}