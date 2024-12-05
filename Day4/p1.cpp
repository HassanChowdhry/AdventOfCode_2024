#include <bits/stdc++.h>
using namespace std;

#define flash ios_base::sync_with_stdio(false);cin.tie(NULL);
#define loop(n) for(int i=0;i<n;++i)
#define ln "\n"

void solve() {
  int n = 140;
  vector<string> lines(n+8); 
  string pad = "";
  for (int i = 0; i < 148; i++) {
    pad += "#";
  }
  
  lines[0] = pad; lines[1] = pad; lines[2] = pad; lines[3] = pad;
  lines[n + 8 -1] = pad; lines[n + 8 -2] = pad; lines[n + 8 - 3] = pad; lines[n + 8 - 4] = pad;

  for (int i = 4; i < n+4; i++) {
    lines[i] = "####";
    string s;
    cin >> s;
    lines[i] += s + "####";
  }

  int total = 0;
  for (int i = 4; i < n + 4; i++) {
    for (int j = 4; j < n + 4; j++) {
      if (lines[i][j] != 'X') continue;

      int curr = 0;

      if (lines[i][j] == 'X' && lines[i][j+1] == 'M' && lines[i][j+2] == 'A' && lines[i][j+3] == 'S')
        ++curr;
 
      if (lines[i][j] == 'X' && lines[i][j-1] == 'M' && lines[i][j-2] == 'A' && lines[i][j-3] == 'S')
        ++curr;
 
      if (lines[i][j] == 'X' && lines[i+1][j] == 'M' && lines[i+2][j] == 'A' && lines[i+3][j] == 'S')
        ++curr;
 
      if (lines[i][j] == 'X' && lines[i-1][j] == 'M' && lines[i-2][j] == 'A' && lines[i-3][j] == 'S')
        ++curr;
      
      if (lines[i][j] == 'X' && lines[i+1][j+1] == 'M' && lines[i+2][j+2] == 'A' && lines[i+3][j+3] == 'S')
        ++curr;

      if (lines[i][j] == 'X' && lines[i-1][j-1] == 'M' && lines[i-2][j-2] == 'A' && lines[i-3][j-3] == 'S')
        ++curr;

      if (lines[i][j] == 'X' && lines[i+1][j-1] == 'M' && lines[i+2][j-2] == 'A' && lines[i+3][j-3] == 'S')
        ++curr;

      if (lines[i][j] == 'X' && lines[i-1][j+1] == 'M' && lines[i-2][j+2] == 'A' && lines[i-3][j+3] == 'S')
        ++curr;
      

      total += curr;
    } 
  }

  cout << total;
}

int main() {
  flash;
  solve();
  return 0;
}