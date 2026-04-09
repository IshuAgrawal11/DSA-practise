n = int(input("Enter the number of terms: "))
# sum = 0
# for i in range (1, n + 1):
#     sum += i
# print(sum)

'''fibonacci series is a series of numbers where each number is the sum of the two preceding 
   ones, usually starting with 0 and 1.'''

for i in range (n):
    if i <= 1:
        print(i, end = " ")
    else:
        a, b = 0, 1
        for j in range (2, i + 1):
            c = a + b
            a = b
            b = c
        print(c, end = " ")