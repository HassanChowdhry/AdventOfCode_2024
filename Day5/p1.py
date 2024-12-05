# n, m = 1176, 202
n, m = 21, 6

pre = {}

arr = [input().split('|') for _ in range(n)]
for s, e in arr:
  if s not in pre:
    pre[s] = []
  if e not in pre:
    pre[e] = []
  pre[e].append(s)

arr = [input().split(',') for _ in range(m)]
valid = []

def is_valid(nums):
  for i in range(len(nums)):
    check = nums[:i]
    for num in pre[nums[i]]:
      if num not in check and num in nums:
        return False
  return True

for nums in arr:
  if is_valid(nums):
    valid.append(nums)

total = 0
for arr in valid:
  total += int(arr[len(arr) // 2])

print(total)