n = int(input("Enter the binary number: "))
ans = ""
for i in range (1, n + 1):
    ans += f"{i:b}"
ans = (int(ans, 2))
print(ans % ((10**9) + 7))

