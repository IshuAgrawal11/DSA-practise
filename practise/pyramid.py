n = int(input("Enter the number of rows: "))
for i in range (1, n + 1):
    print(" " * (n - i) * 2, end = "")
    for j in range (1, i + 1):
        print(j, end = " ")

    for k in range (2, i + 1):
        print(i-1, end = " ")
        i -=1
    print()