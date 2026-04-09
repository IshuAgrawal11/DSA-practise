n = int(input("Enter the number: "))
list = []
ans = 0
i = 0
while n > 0:
    bit = n % 10
    if bit == 1:
        ans = ans + (2**i)
    i += 1
    n = n // 10
    
print(ans)
