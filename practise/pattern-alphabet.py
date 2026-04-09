n = int(input("Enter the number of rows: "))
# for i in range (1, n + 1):
#     for j in range (1, i + 1):
#         char = chr(ord('A') + n - i + j - 1)
#         print(char, end = " ")
        
#     print()


for i in range (1, n + 1):
    char = ord('A') + n - i
    for j in range (1, i + 1):
        print(chr(char), end = " ")
        char += 1
    print()

for i in range (1, n + 1):
    for j in range (1, n + 1):
        print(chr(ord('A') + i + j - 2), end = " ")
        
    print()