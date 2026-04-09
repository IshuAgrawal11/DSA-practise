n = int(input("Enter the number of rows: "))
digits = []
while n > 0:
    digit = n % 10
    digits.append(digit)
    n //= 10


print("Digits in reverse order:", digits)
print("Digits in original order:", digits[::-1])

sum = sum(digits)
print("Sum of digits:", sum)
product = 1
for digit in digits:
    product *= digit
print("Product of digits:", product)
print("Difference between product and sum:", product - sum)