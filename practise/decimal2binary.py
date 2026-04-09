n = int(input("Enter the number of rows: "))
bits = 16
mask = (1 << bits) - 1
n = n & mask
ans = 0
i = 0
# binary = []
while n != 0:
    bit = n & 1
    # print(bit)
    ans = bit * (10 ** i) + ans
    # binary.append(bit)
    n = n >> 1
    i += 1
print(ans)
# print(int("".join(map(str, binary[::-1]))))
