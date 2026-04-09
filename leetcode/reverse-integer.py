def reverseInt():
    n = int(input("Enter the number: "))
    sign = -1 if n < 0 else 1
    n = abs(n)
    ans = 0
    while n != 0:
        digit = n % 10
        n //= 10
        ans = (ans * 10) + digit
    ans *= sign
    if ans > (2**31) - 1 or ans < -2**31:
        return 0
    return ans
print(reverseInt())
print(reverseInt())
