n = int(input("Enter an Integer number: "))
# # n = bin(n).replace("0b", "")
n_bin = f"{n:b}"
ans = n ^ ((1 << len(n_bin)) - 1)
print(f"{ans:b}")
print(ans)

# second approach
b = bin(n) 
print(b)
res = ""
for c in b[2:]:
    if c == "1":
        res += "0"
    else:
        res += "1"
print(int(res, 2))

# third approch
mask = (1 << n.bit_length()) - 1
result = (~n) & mask
print(f"Flipped 5: {result}")