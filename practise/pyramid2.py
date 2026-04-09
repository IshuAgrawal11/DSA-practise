n = int(input("Enter the number of rows: "))
for i in range (n, 0, -1):
    num = i
    for j in range (1, i + 1):
        print(j, end = " ")

    print("* " * (n - i) * 2, end = "")

    for k in range (0, i):
        print(num, end = " ")
        num -= 1
    print()