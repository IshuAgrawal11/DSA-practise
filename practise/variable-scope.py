n = int(input("Enter the number: "))
num = str(n)

# index based approach
# for i in range (len(num)):
#     print(int(num[i]))

# direct approach
sum = 0
product = 1
for i in num:
    digit = int(i)
    sum += digit
    product *= digit
print("Sum of digits:", sum)
print("Product of digits:", product)
print("Difference between product and sum:", product - sum)