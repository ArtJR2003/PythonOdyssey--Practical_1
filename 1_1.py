ls = [1, 4, 15, 3, 40, 28, 7, 8, 9]
print(f"Our list is: {ls}")
max = ls[0]
for i in range(1, len(ls)):
  if max < ls[i]:
    max = ls[i]
print(f"Our maximum value is: {max}")
