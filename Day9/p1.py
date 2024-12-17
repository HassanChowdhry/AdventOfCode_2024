arr = input()
n = len(arr)
# print(arr)
# print(n)
res = []
id = 0
for i in range(n):
  if i % 2: res += ['.'] * int(arr[i])
  else: res += [str(id)] * int(arr[i]); id+=1

l, r = 0, len(res)-1
while l < r:
  while res[l] != '.': l+=1
  while res[r] == '.': r-=1
  
  res[l], res[r] = res[r], res[l]
  l+=1; r-=1

checksum = 0
id = 0
for i in range(len(res)):
  if res[i] == '.': continue
  checksum += id * int(res[i])
  id += 1

print(checksum)

# 6310675819476