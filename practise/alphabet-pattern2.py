n = int(input("Enter the number of rows: "))
# for i in range (1, n + 1):
#     for j in range (0, n):
#         print(chr(ord('A')+j), end = " ")
#     print()

# num = 0
# for i in range (1, n + 1):
#     for j in range (0, n):
#         print(chr(ord('A')+num), end = " ")
#         num += 1
#     print()

for i in range (0, n):
    for j in range (0, i + 1):
        print(chr(ord('A')+i), end = " ")
        i += 1
    print()
