n = int(input("Enter the number of rows: "))
for i in range (1, n + 1):
    print(" " * (n - i), end = "")
    print("* " * i, end = "")
    print()

for i in range (1, n):
    print(" " * (i), end = "")
    print("* " * (n - i), end = "")
    print()