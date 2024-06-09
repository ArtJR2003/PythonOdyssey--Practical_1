size = int(input("Enter a size of the list: "))
ls = []
for i in range(size):
  digit = input(f"Enter valid digit for {i} position: ")
  if digit.isdigit():
    ls.append(digit)
  else:
    print("Not a number")
    break

print(ls)
