n = int(input("Enter the number of rows: "))
for i in range (1, n + 1):
    print("* " * (n - i + 1), end = " ")
    print()


for i in range (1, n + 1):
    print(" " * (i -1) * 2, end = "")
    print(f"{i} " * (n - i + 1), end = " ")
    print()

for i in range (1, n + 1):
    print(" " * (n -i) * 2, end = "")
    print(f"{i} " * i, end = " ")
    print()
 
 