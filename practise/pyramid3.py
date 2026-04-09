n = int(input("Enter the no. of Rows: "))
for i in range (1, n + 1):  
    print(" " * (n - i) * 2, end = "")
    print("* " * i, end = "")
    print("* " * (i - 1), end = "")
    print()


for i in range (1, n + 1):
    print(" " * (i - 1) * 2, end = "")
    print("* " * (n - i + 1), end = "")
    print("* " * (n - i), end = "")
    print()