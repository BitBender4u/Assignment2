def dictn(i):
  for sxn, value in i.items():
    if value % 2 == 0:
      print(sxn)

#example
i={'a':2, 'b':3, 'c':4}
dictn(i)
