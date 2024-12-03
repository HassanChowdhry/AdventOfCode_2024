n = 1000
arr = [input().split() for _ in range(n)]

safe = 0
for a in arr:
  prev = int(a[0])
  inc = dec = True
  for num in a[1:]:
    num = int(num)
    inc = inc and (num > prev and (1 <= (num - prev) <= 3))
    dec = dec and (num < prev and (1 <= (prev - num) <= 3))
    prev = num

  if inc or dec:
    safe += 1

print(safe)