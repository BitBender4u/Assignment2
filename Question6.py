def nums(ints):
  largest =ints[0]
  for i in ints:
    if i > largest :
      largest =i
  return largest

#example
ints=(10,20,30,40,50)
print(nums(ints))
