ls = [1, 4, 15, 3, 40, 28, 7, 8, 9]
print(f"This is our list: {ls}")
min = ls[0]
for i in range(1, len(ls)):
  if min > ls[i]:
    min = ls[i]
min_index = ls.index(min)
print(f"This is our minimum value's index: {min_index}")
