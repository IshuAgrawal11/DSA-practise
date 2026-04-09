n = int(input("Enter the number of rows: "))
bits = 16
ans = 0
i = 0
if n < 0:
    value = n & ((1 << bits) - 1)
    print(value)
    n = abs(n)
    n = n ^ ((1 << bits) - 1)
    print(n)
    twos_complement = n + 1
    n = twos_complement
    print(n)
while n != 0:
    bit = n & 1
    ans = bit * (10 ** i) + ans
    n = n >> 1
    i += 1
print(ans)
