n = 1000
arr = [input().split() for _ in range(n)]

safe = 0
for a in arr:
  for ignore in range(len(a)):
    prev = None
    inc = dec = True
    
    for i in range(len(a)):
      if i == ignore: continue
      num = int(a[i])
      if not prev:
        prev = num; continue
        
      inc = inc and (num > prev and (1 <= (num - prev) <= 3))
      dec = dec and (num < prev and (1 <= (prev - num) <= 3))
      prev = num

    if inc or dec:
      safe += 1
      break

print(safe)