n = int(input("Enter the number of rows: "))
for i in range (1, n + 1):
    for j in range (1, n + 1):
        print(j, end = " ")
    print()

# for i in range (1, n + 1):
#     for j in range (1, n + 1):
#         print(i, end = " ")
#     print()

# for i in range (1, n + 1):
#     for j in range (n, 0, -1):
#         print(j, end = " ")
#     print()

# for i in range (1, n + 1):
#     for j in range (1, n + 1):
#         print(n - j + 1, end = " ")
#     print()

# for i in range (1, n + 1):
#     for j in range (1, n + 1):
#         print(n - i + 1, end = " ")
#     print()

for i in range (n, 0, -1):
    for j in range (1, n + 1):
        print(i, end = " ")
    print()