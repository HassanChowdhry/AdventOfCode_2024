#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back
#define fs first 
#define sc second 
#define all(a) a.begin(),a.end()
#define flash ios_base::sync_with_stdio(false);cin.tie(NULL);
#define test int t;cin>>t;while(t--)
#define loop(n) for(int i=0;i<n;++i)
#define loopx(x, n) for(int i=x;i<n;++i)
#define input(arr,n);for(int i=0;i<n;++i)cin>>arr[i];
#define ln "\n"

void solve() {
  string s = "";
  char c;
  int doo = 1;
  while (scanf("%c", &c) != EOF) {
    s += c;
  }
  s += "####################";

  int n = s.length(), res = 0;

  auto get_number = [&](int& i) {
    int x = 0;
    while (isdigit(s[i])) {
      x = 10 * x + (s[i] - '0');
      ++i;
    }
    if (1 <= x <= 999) {
      return x;
    }
    return -1;
  };

  int x, y;
  loop(n) {
    if (s[i] == 'd' && s[i+1] == 'o' && s[i+2] == 'n' && s[i+3] == '\'' && s[i+4] == 't' && s[i+5] == '(' && s[i+6] == ')') {
      doo = 0; i+=6; continue;
    }
    if (s[i] == 'd' && s[i+1] == 'o' && s[i+2] == '(' && s[i+3] == ')') {
      doo = 1; i+=3; continue;
    }

    if (!doo) continue;

    if (s[i] == 'm' && s[i+1] == 'u' && s[i+2] == 'l' && s[i+3] == '(') {
        i+=4;
       
        x = get_number(i); if (x == -1) break;
        
        if (s[i] == ',') {
          i++;
          y = get_number(i); if (y == -1) break;
          
          if (s[i] == ')')
            res += x * y;
        }
    }
  }

  cout << res;

}

int main() {
  solve();
  return 0;
}