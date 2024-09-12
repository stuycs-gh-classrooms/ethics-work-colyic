def max_end3(nums):
  num = 0

  if nums[0] > nums[-1]:
    num = nums[0]
  else:
    num = nums[-1]

  for i in range(len(nums)):
    nums[i] = num
  return nums
