n = int(input("Enter the number of rows: "))
# num = 1           
# for i in range (1, n + 1):
#     for j in range (1, i + 1):
#         print(num, end = " ")
#         num += 1
#     print()

# for i in range (1, n + 1):
#     for j in range (1, i + 1):
#         print(f"{i:02d}", end = " ")
#         i += 1
#     print()

for i in range (n, 0, -1):
    for j in range (1, i + 1):
        print(f"{i:02d}", end = " ")
        i -= 1
    print()