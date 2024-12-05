#include <bits/stdc++.h>
using namespace std;

#define flash ios_base::sync_with_stdio(false);cin.tie(NULL);
#define loop(n) for(int i=0;i<n;++i)

void solve() {
  string s = "";
  char c;
  while (scanf("%c", &c) != EOF) {
    s += c;
  } s += "####################";

  int n = s.length(), res = 0;

  auto get_number = [&](int& i) {
    int x = 0;
    while (isdigit(s[i])) {
      x = 10 * x + (s[i] - '0'); ++i;
    }

    if (1 <= x <= 999) return x;
    
    return -1;
  };

  int x, y;
  loop(n) {
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
  flash;
  solve();
  return 0;
}