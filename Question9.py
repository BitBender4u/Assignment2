def myFun(nums, target_sum):
  seen = set()
  for num in nums:
    complement = target_sum - num
    if complement in seen:
      return True
    seen.add(num)
  return False


# Example usage
nums = [1, 2, 3, 4, 5]
target_sum = 7
print(myFun(nums, target_sum))  # Output: True
