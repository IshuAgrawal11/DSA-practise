# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
n = int(input())
# The correct way to mask 32 bits using shifts:
binary_output = f"{n:032b}"
print(binary_output)
binary_output = binary_output[::-1]
# binary_output = str(binary_output)
# binary_output = int(binary_output[::-1])
print(binary_output)
ans = 0
i = 0
while binary_output != 0:
    digit = binary_output % 10
    if digit == 1:
        ans = (2**i) + ans
    i += 1
    binary_output //= 10
print(ans)
