n, m = input().split()
n, m = int(n), int(m)

arr = [list(input()) for _ in range(n)]

dir = {
  "^": ">",
  ">": "v",
  "v": "<",
  "<": "^",
}

move = {
  "^": (-1, 0),
  ">": (0, 1),
  "v": (1, 0),
  "<": (0, -1)
}

o_pos = 0, 0
for i in range(n):
  for j in range(m):
    if arr[i][j] == "^":
      o_pos = i, j; break

total = 0
for i in range(n):
  for j in range(m):
    if arr[i][j] == '#' or arr[i][j] == '^':
      continue
    
    arr[i][j] = '#'
    obs = set()
    end = False
    curr = "^"
    pos = o_pos
    visit = set()
    visit.add(pos)

    while not end:
      next_pos = pos[0] + move[curr][0], pos[1] + move[curr][1]
      pi, pj = next_pos

      if arr[pi][pj] == "." and (pi == 0 or pj == 0 or pi == n-1 or pj == m-1):
        visit.add((pi, pj)); end = True; break
      elif arr[pi][pj] == '#':
        if (pi, pj, curr) in obs:
          total += 1; end = True; break
        obs.add((pi, pj, curr))
        curr = dir[curr]
      else:
        visit.add((pi, pj))
        pos = next_pos
    arr[i][j] = '.'

print(total)
