array = [1, 2, 3, 4, 5]
print(sum(array))

power = int(input("Enter the power of two: "))
while power % 2 == 0:
    power //= 2
if power ==1:
    print("True")
else:
    print("False")

binary = f"{power:b}"
print(binary)