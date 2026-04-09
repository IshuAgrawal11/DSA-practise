def findKthBit(n: int, k: int) -> str:
    if n == 1:
        return "0"
    
    mid = 1 << (n - 1)
    
    if k == mid:
        return "1"
    elif k < mid:
        return findKthBit(n - 1, k)
    else:
        # If k is in the second half, find the mirrored bit in S(n-1) and invert it
        # The mirrored index is: total_length - k + 1
        # total_length = (1 << n) - 1
        mirrored_bit = findKthBit(n - 1, (1 << n) - k)
        return "1" if mirrored_bit == "0" else "0"

# Example Usage:
# n = 4, k = 11
print(f"The 11th bit of S4 is: {findKthBit(4, 11)}")