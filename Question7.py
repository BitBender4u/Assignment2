def remove_duplicates(i):
  list=[]
  for items in i:
    if items not in list:
      list.append(items)
  return list

#example
i=[1,22,3,3,12,6,6,7,7,8]
print(remove_duplicates(i))
