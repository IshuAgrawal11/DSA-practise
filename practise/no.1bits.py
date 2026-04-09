n = int(input("Enter the number: "))
# fastest method to count the number of 1's in the binary representation of n
count = n.bit_count()
print(count)

# the string method to count the number of 1's in the binary representation of n
binary_representation = bin(n)  
print("Binary representation:", binary_representation)
count = binary_representation.count('1')
print("Number of 1's in binary representation:", count)

# The "Brian Kernighan’s Algorithm" (Manual Way) that repeatedly flips the least significant set bit of the number to zero and counts how many times this operation is performed until the number becomes zero.
count = 0
while n > 0:
    n = n & (n - 1)
    count += 1
print("Number of 1's using Brian Kernighan's Algorithm:", count)