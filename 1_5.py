ls = [4, 50, -23, 5.2, -144, 12]
print(f"This is our list: {ls}")
min = ls[0]
max = ls[0]
for i in range(1, len(ls)):
  if min > ls[i]:
    min = ls[i]
  elif max < ls[i]:
    max = ls[i]
  else:
    pass
print(f"Our maximum and minimum values' summary is: {min + max}")
