arr = input()
n = len(arr)
# print(arr)
# print(n)
res = []
id = 0
for i in range(n):
  if i % 2: res += ['.'] * int(arr[i])
  else: res += [str(id)] * int(arr[i]); id+=1

def rindex(arr, el): return len(arr) - 1 - arr[::-1].index(el)
def lastcontindex(arr, start):
    ind = start
    while arr[ind] == '.': ind += 1
    return ind - 1

l, r = 0, len(res)-1
prev = None
while l < r:
  while res[l] != '.': l+=1
  while res[r] == '.' or res[r] == prev: r-=1
  prev = res[r]
  findex, pindex = res.index(res[r]), lastcontindex(res, l)
  lenr, lenl = r - findex + 1, pindex - l + 1
  pl = pindex + 1
  
  while lenl < lenr and pl < r:
    pl = pindex + 1
    while pl < r and res[pl] != '.':
      pl += 1
    if pl >= r: break
    pindex = lastcontindex(res, pl)
    lenl = pindex - pl + 1
  if pl >= r: continue
  for i in range(lenr):
    res[pl + i], res[r - i] = res[r - i], res[pl + i]
  
print(res)

checksum = 0
id = 0
for i in range(len(res)):
  if res[i] == '.': continue
  checksum += id * int(res[i])
  id += 1

print(checksum)

# 6310675819476