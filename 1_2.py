ls = [1, 4, 15, 3, 40, 28, 7, 8, 9]
print(f"Our list is: {ls}")
min = ls[0]
for i in range(1, len(ls)):
  if min > ls[i]:
    min = ls[i]
print(f"Our minimum value is: {min}")
