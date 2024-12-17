n = 50
arr = [input() for _ in range(n)]
antinodes = set()
antennas = {}

for i in range(n):
  for j in range(len(arr[i])):
    if arr[i][j] != '.':
      antenna = arr[i][j]
      antinodes.add((i, j))
      if antenna not in antennas:
        antennas[antenna] = []
      antennas[antenna].append((i, j))

for key, value in antennas.items():
  for ant1 in value:
    for ant2 in value:
      if ant1 == ant2: continue
      offset = (-ant1[0] + ant2[0], -ant1[1] + ant2[1])
      anti = (ant1[0] - offset[0], ant1[1] - offset[1])
      while (not (anti[0] < 0 or anti[0] >= n or anti[1] < 0 or anti[1] >= len(arr[0]))): 
        antinodes.add(anti)
        anti = (anti[0] - offset[0], anti[1] - offset[1])

# print(antinodes)
print(len(antinodes))