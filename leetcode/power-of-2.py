# first approach
n = int(input("Enter the number: "))
i = 1
found = False
if n <= 0:
    print("False")
elif n == 1:
    print("True")
elif n % 2 != 0:
    print("False")    
else:
    num = 0
    while num < n:
        num = 2**i
        if num == n:
            print("True")
            found = True
            break
        i += 1
    
    if not found:
        print("False")
print(f"Power (i): {i}")

# second approach
def is_power_of_two(n):
    if n <= 0: return False
    return (n & (n - 1)) == 0
print(is_power_of_two(n))

# third approach
def isPowerOfTwo(n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n //= 2
        return n == 1
