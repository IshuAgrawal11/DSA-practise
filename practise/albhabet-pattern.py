n = int(input("Enter the number of rows: "))
# for i in range (0, n):
#     for j in range (0, i + 1):
#         print(chr(ord('A')+i), end = " ")
#     print(  )

# for i in range (n, 0, -1):
#     for j in range (0, i):
#         print(chr(ord('A')+i - 1), end = " ")
#     print()

for i in range (0, n):
    for j in range (0, n - i):
        print(chr(ord('A')+i), end = " ")
    print()