n, m = input().split()
n, m = int(n), int(m)

arr = [list(input()) for _ in range(n)]
visit = set()

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

pos = 0, 0
for i in range(n):
  for j in range(m):
    if arr[i][j] == "^":
      visit.add((i, j)); pos = i, j; break

end = False
curr = "^"
while not end:
  next_pos = pos[0] + move[curr][0], pos[1] + move[curr][1]
  
  pi, pj = next_pos
  if arr[pi][pj] == "." and (pi == 0 or pj == 0 or pi == n-1 or pj == m-1):
    visit.add((pi, pj)); end = True; break
  elif arr[pi][pj] == '#':
    curr = dir[curr]
  else:
    visit.add((pi, pj))
    pos = next_pos

print(len(visit))
