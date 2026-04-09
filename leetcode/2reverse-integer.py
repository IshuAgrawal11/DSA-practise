def reverse(x: int):
    x = str(x)

    is_negative = False
    if x[0] == "-":
        x = x[1:]
        is_negative = True

    x = int(x[::-1])

    if is_negative == True:
        x = -x

    if x > 2**31-1 or x < -2**31:
        return 0
    else:
        return x
# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))

print(reverse(546))

