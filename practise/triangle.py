n = int(input("Enter the number of rows: "))
for i in range (1, n + 1):
    for j in range (1, i+ 1):
        print(j, end = " ")
    print()

# for i in range (1, n + 1):
#     for j in range (1, n + 1 ):
#         if j <= i:
#             print("*", end = " ")
#         else:
#             print(" ", end = "")
#     print()

# for i in range (1, n + 1):
#     for j in range (1, n + 1):
#         if j <= n - i + 1:
#             print("*", end = " ")
#         else:
#             print(" ", end = "")
#     print()

for i in range (n, 0, -1):
    for j in range (1, i+ 1):
        print("*", end = " ")    
    print()     
    