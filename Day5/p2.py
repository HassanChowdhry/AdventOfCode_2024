from collections import deque
n, m = 1176, 202
# n, m = 21, 6

pre = {}

arr = [input().split('|') for _ in range(n)]
for s, e in arr:
  if s not in pre:
    pre[s] = []
  if e not in pre:
    pre[e] = []
  pre[e].append(s)

arr = [input().split(',') for _ in range(m)]
invalid = []

def is_valid(nums):
  for i in range(len(nums)):
    check = nums[:i]
    for num in pre[nums[i]]:
      if num not in check and num in nums:
        return False
  return True

for nums in arr:
  if not is_valid(nums):
    invalid.append(nums)

def get_res(arr):
  res = []
  for num in arr:
    dfs(num, res, arr)
  return res

def dfs(num, res, arr):
  if num not in arr or num in res:
    return
  
  for preq in pre[num]:
    dfs(preq, res, arr)
  
  if num in arr and num not in res:
    res.append(num)

valid = []
for aaa in invalid:
  curr = get_res(aaa)
  valid.append(curr)
  
# print(valid)
total = 0
for arr in valid:
  total += int(arr[len(arr) // 2])

print(total)