n = int(input("Enter the number of rows: "))
# num = 1
# for i in range (1, n + 1):
#     for j in range (1, n + 1):
#         print(num, end = " ")
#         num += 1
#     print()

# reverse increment
# num = n * n 
# for i in range (1, n + 1):
#     for j in range (1, n + 1):
#         print(f"{num:02d}", end = " ")
#         num -= 1
#     print()

#snake pattern
num = 1
for i in range (1, n + 1):
    for j in range (1, n + 1):
        if i % 2 != 0:
            print(f"{num:02d}", end = " ")
            num += 1
        else:
            print(f"{(i - 1) * n + (n - j + 1):02d}", end = " ")
            num += 1
    print()