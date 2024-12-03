#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back
#define flash ios_base::sync_with_stdio(false);cin.tie(NULL);
#define loop(n) for(int i=0;i<n;++i)
#define ln "\n"

void solve() {
  int n = 1000, l, r;
  vector<int> left;
  unordered_map<int, int> right;
  loop(n) {
    cin >> l >> r;
    left.pb(l); right[r]++;
  }

  ll ans = 0;
  for (int x: left) 
    { ans += abs(x * right[x]); }

  cout << ans;
}

int main() {
  flash;
  solve();
  return 0;
}