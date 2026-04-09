n = int(input("Enter the number of rows: "))
for i  in range (n, 0, -1):
    num = n - i + 1
    print(" " * (n - i) * 2, end = "")
    for j in range (1, i + 1):
        print(num, end = " ")
        num += 1
    print()

for i  in range (1, n + 1):
    num = n
    print(" " * (n - i) * 2, end = "")
    for j in range (1, i + 1):
        print(num, end = " ")
        num -= 1
    print()

# for i in range (n, 0, -1):
#     num = n
#     print(" " * (n - i) * 2, end = "")
#     for j in range (1, i + 1):
#         print(num, end = " ")
#         num -= 1
#     print()

num = 1
for i in range (1, n + 1):
    print(" " * (n - i) * 2, end = "")
    for j in range (1, i + 1):
        print(num, end = " ")
        num += 1
    print()