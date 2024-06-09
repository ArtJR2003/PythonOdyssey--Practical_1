ls = [4, 50, -23, 5.2, -144, 12]
print(f"This is our list: {ls}")
for i in range(len(ls)):
  ls[i] = ls[i] / len(ls)
print(f"This is our updated list: {ls}")
