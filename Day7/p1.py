n = 850
arr = [input().split(": ") for _ in range(n)]

memo = {}
def checkall(target, curr, i, nums_cache, nums):
  if curr == target:
    return 1
  if curr > target or i >= len(nums):
    return 0
  res = 0
  res += checkall(target, curr + int(nums[i]), i+1, nums_cache, nums)
  if curr == 0: curr = 1
  res += checkall(target, curr * int(nums[i]), i+1, nums_cache, nums)
  return res
  
x = 0
for i in range(n):
  if (checkall(int(arr[i][0]), 0, 0, arr[i][1], arr[i][1].split()) > 0):
    x += int(arr[i][0])

print(x)
    