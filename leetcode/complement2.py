n =  int(input("Enter the number: "))
mask = 0
m = n

if n == 0:
    print("1")

while m != 0:
    mask = mask << 1 | 1
    m = m >> 1

ans = (~n) & mask
print(ans)

