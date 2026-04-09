n = int(input("Enter the number: "))
bit = f"{n:b}"
print(bit)
ans = ""
for i in bit:
    if i == "0":
        ans += "1"
    else:
        ans += "0"
print(ans)
print(int(ans, 2))

# second approach

if n == 0:
    print(1)
num_bits = n.bit_length()
mask = (1 << num_bits) - 1
result = n ^ mask
print(f"Flipped 5: {result}")
print(result)

    