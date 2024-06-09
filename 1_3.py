ls = [1, 4, 15, 3, 40, 28, 7, 8, 9]
print(f"This is our list: {ls}")
max = ls[0]
for i in range(1, len(ls)):
  if max < ls[i]:
    max = ls[i]
max_index = ls.index(max)
print(f"This is our maximum value's index: {max_index}")
