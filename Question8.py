def greater(i,n):
  result=[]
  for key, value in i.items():
    if value>n:
      result.append(key)
  return result

#example
d={'a':5, 'b':12, 'c':3}
n=4
print(greater(d,n))
